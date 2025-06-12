from django.db import models     # type: ignore
import uuid
from users.models import User
from users.models import Staff

class RoomType(models.Model):
    ROOM_TYPES = [
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('DELUXE', 'Deluxe'),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    max_occupancy = models.IntegerField()
    amenities = models.TextField()
    img = models.ImageField(upload_to='room_types/', null=True, blank=True)
    def __str__(self):
        return self.name
    

class Room(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('OCCUPIED', 'Occupied'),
        ('MAINTENANCE', 'Under Maintenance'),
        ('CLEANING', 'Cleaning'),
    ]
    
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    floor = models.IntegerField()
    amenities = models.TextField()
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    max_occupancy = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')

   
    def __str__(self):
        return f"Room {self.room_number} ({self.room_type.name})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('CHECKED_OUT', 'Checked Out'),
    ]
    customer = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    special_requests = models.TextField(null=True, blank=True)  
    def __str__(self):
        return f"{self.guest.name} - {self.room.room_number} ({self.status})"
    

    
class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CREDIT_CARD', 'Credit Card'),
        ('DEBIT_CARD', 'Debit Card'),
        ('CASH', 'Cash'),
        ('ONLINE', 'Online Payment'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.booking} - {self.amount}"

class Review(models.Model):
    room = models.ForeignKey(Room, null=True,on_delete=models.CASCADE)
    customer = models.ForeignKey(User,null=True, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    rating = models.IntegerField()  # 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)            

    def __str__(self):
        return f"{self.guest.name}'s review for Room {self.room.room_number}"



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"

class HotelInfo(models.Model):
    about_text = models.TextField()
    established_year = models.IntegerField(default=2000)
    location = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    social_media_links = models.JSONField(default=dict)  # Store as JSON
    logo = models.ImageField(upload_to='hotel_logo/', null=True, blank=True)
    privacy_policy = models.TextField(blank=True)
    terms_conditions = models.TextField(blank=True)

    def __str__(self):
        return "Hotel Info"

class CheckInRecord(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Check-in for {self.booking}"


class BiometricAttendance(models.Model):
    employee = models.ForeignKey(Staff, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"


class Procurement(models.Model):
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=200)
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.item_name
    
class POS(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('PAID', 'Paid'), ('PENDING', 'Pending')])
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"POS for {self.booking} - {self.total_amount}"
    

class From_Builder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
    
    
class CoworkingSpace(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name


class  Security_Guards(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    assigned_area = models.CharField(max_length=200)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()

    def __str__(self):
        return self.name
    
class Sports_Club(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name

class Locker_and_Safe(models.Model):
    locker_number = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.locker_number
    
class Garage_and_Workshop(models.Model):
    workshop_name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.workshop_name
    
class Newspaper(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Property_Management(models.Model):
    property_name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.property_name
    
class Eldery_Care(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Hospital (models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Optical_and_Eye_Care(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name
    

class Medical_Lab(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name
    

class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name
    
class Beauty_Spa(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name
    

class Beverage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Facilities(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Suport_Ticket(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket from {self.customer.name} - {self.subject}"
    

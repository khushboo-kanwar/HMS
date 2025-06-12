from django.db import models # type: ignore
import uuid
# from restaurant.models import Restaurant
from hotel.models import Room
from users.models import Staff

class ServiceCategory(models.Model):
    LAUNDRY = 'laundry'
    HOUSEKEEPING = 'housekeeping'
    CLEANING = 'cleaning'
    DELIVERY = 'delivery'
    Restaurant= 'restaurant'


    CATEGORY_CHOICES = [
        (LAUNDRY, 'Laundry'),
        (HOUSEKEEPING, 'Housekeeping'),
        (CLEANING, 'Cleaning'),
        (DELIVERY, 'Delivery'),
        (Restaurant, 'Restaurant'),
    ]
    
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=LAUNDRY)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()  
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ServiceBooking(models.Model): 
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=15)
    booking_date = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.guest_name} - {self.service.name} on {self.booking_date}"
    
class ServicePayment(models.Model):
    service_booking = models.ForeignKey(ServiceBooking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')])
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.service_booking} - {self.amount}"
    

class ServiceReview(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    rating = models.IntegerField()  # 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.guest_name}'s review for {self.service.name}"    
    

class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.ImageField(upload_to='social_icons/', null=True, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class ContactMessage(models.Model):
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)  

    def __str__(self):
        return f"Message from {self.guest_name} on {self.created_at}"


class RoomCleaningLog(models.Model):
    room = models.ForeignKey(Room,null=True, on_delete=models.CASCADE)
    cleaned_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'HOUSEKEEPING'})
    cleaned_at = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.room.room_number} cleaned at {self.cleaned_at}"


class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    percentage = models.PositiveIntegerField()  
    valid_from = models.DateField()
    valid_to = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.code})"
    

class Recruitment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    application_deadline = models.DateField()
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Job_search(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    application_deadline = models.DateField()
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Movie_and_TV(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title
    
class Movie_show_booking(models.Model):
    movie = models.ForeignKey(Movie_and_TV, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=15)
    booking_date = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.guest_name} - {self.movie.title} on {self.booking_date}"
    
class Water_park(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=100)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_open = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    

class GYM_management(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=100)
    membership_fee = models.DecimalField(max_digits=10, decimal_places=2)
    is_open = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    

class Constriction(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200) 
    project_cost = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title       
    

class Fleet(models.Model):
    vehicle_type = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.vehicle_type} - {self.license_plate}"
    


class Vehicle_Trade(models.Model):
    vehicle = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    trade_type = models.CharField(max_length=100)
    trade_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vehicle} - {self.trade_type} on {self.trade_date}"
    

class Vehicle_booking(models.Model):
    vehicle = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=15)
    booking_date = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.guest_name} - {self.vehicle} on {self.booking_date}"
       

class Car_Dealership(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()
    description = models.TextField()
    def __str__(self):
        return self.name        
    
class Tailoring_and_Fashion_design(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    opening_hours = models.CharField(max_length=100)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title
    

class Dairy_Cattle(models.Model):
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    health_status = models.CharField(max_length=100)
    is_available_for_sale = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.breed} - {self.age} years"
    

class Mobile_Service(models.Model):
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.service_type
    
class Vehicle_Inspection(models.Model):
    vehicle = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    inspection_date = models.DateTimeField(auto_now_add=True)
    inspector_name = models.CharField(max_length=200)
    inspection_report = models.TextField()

    def __str__(self):
        return f"Inspection for {self.vehicle} on {self.inspection_date}"
    
class Machine_Repair(models.Model):
    machine_type = models.CharField(max_length=100)
    repair_date = models.DateTimeField(auto_now_add=True)
    repair_description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Repair for {self.machine_type} on {self.repair_date}"
    
class Repair (models.Model):
    vehicle = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    repair_date = models.DateTimeField(auto_now_add=True)
    repair_description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Repair for {self.vehicle} on {self.repair_date}"
 
class AI(models.Model):
    user_input = models.TextField()
    ai_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query at {self.timestamp}"

class Catering(models.Model):
    menu = models.TextField()
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Catering service - {self.price_per_person} per person"
    
class Rental(models.Model):
    item_name = models.CharField(max_length=200)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    rental_duration = models.DurationField()  
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Rental item - {self.item_name} for {self.rental_price}"
    

class Sales_Agent(models.Model):
    name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
class Sales_Force(models.Model):
    agent = models.ForeignKey(Sales_Agent, on_delete=models.CASCADE)
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission_earned = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale by {self.agent.name} on {self.sale_date}"
    

class Contract(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    terms_and_conditions = models.TextField()
    is_signed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Documents(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Google_Docs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    google_doc_link = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Custom_Field(models.Model):
    name = models.CharField(max_length=200)
    field_type = models.CharField(max_length=50, choices=[('text', 'Text'), ('number', 'Number'), ('date', 'Date'), ('boolean', 'Boolean')])
    is_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Queue_Management(models.Model):
    queue_number = models.CharField(max_length=20, unique=True)
    guest_name = models.CharField(max_length=200)
    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('waiting', 'Waiting'), ('served', 'Served')], default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Queue {self.queue_number} - {self.guest_name}"
    
class Game_Zone(models.Model):
    game_name = models.CharField(max_length=200)
    description = models.TextField()
    age_limit = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.game_name
    

class Video_Hub(models.Model):
    video_title = models.CharField(max_length=200)
    video_url = models.URLField()
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_title
    
class Photo_and_Studio(models.Model):
    photo_title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/')
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo_title
    
class File_Sharing(models.Model):
    file_title = models.CharField(max_length=200)
    file = models.FileField(upload_to='shared_files/')
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_title
    
class Feedback(models.Model):
    guest_name = models.CharField(max_length=200)
    feedback_text = models.TextField()
    rating = models.IntegerField()  # 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback from {self.guest_name} - {self.rating}"
    

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

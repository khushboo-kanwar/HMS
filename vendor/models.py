from django.db import models # type: ignore
from users.models import User




class Vendor(models.Model): 
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
    
class VendorCategory(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class VendorService(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()  # Duration of the service
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class VendorBooking(models.Model):  
    vendor_service = models.ForeignKey(VendorService, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=15)
    booking_date = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.guest_name} - {self.vendor_service.name} on {self.booking_date}"
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# vendor/models.py

class Quotation(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    customer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    service = models.ForeignKey(VendorService, on_delete=models.CASCADE)
    message = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Quotation from {self.vendor.name} to {self.customer.username}"

# vendor/models.py

class Project(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Sales(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.product.name} by {self.vendor.name}"
    

class Consignment(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    consignment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('delivered', 'Delivered')])

    def __str__(self):
        return f"Consignment of {self.product.name} by {self.vendor.name}"
    


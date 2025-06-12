from django.db import models  # type: ignore
from django.contrib.auth.models import AbstractUser  # type: ignore
from django.dispatch import receiver  # type: ignore
from django.db.models.signals import post_save  # type: ignore


class User(AbstractUser):
    ROLE_CHOICES = [
        ('superadmin', 'Super Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('hotel', 'Hotel'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=20, blank=True, null=True)


class HotelProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)
    location = models.TextField()


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)


class Staff(models.Model):
    ROLE_CHOICES = [
        ('RECEPTIONIST', 'Receptionist'),
        ('HOUSEKEEPING', 'Housekeeping'),
        ('MANAGER', 'Manager'),
        ('CHEF', 'Chef'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    contact = models.CharField(max_length=15)
    img = models.ImageField(upload_to='staff_images/', null=True, blank=True)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()
    emergency_contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    id_proof = models.FileField(upload_to='staff_id_proofs/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.role}"

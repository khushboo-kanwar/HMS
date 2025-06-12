from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver # type: ignore
from .models import User, CustomerProfile, VendorProfile, HotelProfile, StaffProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'customer':
            CustomerProfile.objects.create(user=instance)
        elif instance.role == 'vendor':
            VendorProfile.objects.create(user=instance)
        elif instance.role == 'hotel':
            HotelProfile.objects.create(user=instance)
        elif instance.role == 'staff':
            StaffProfile.objects.create(user=instance)

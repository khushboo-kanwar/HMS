from django.db import models # type: ignore
from django.contrib.auth import get_user_model # type: ignore
User = get_user_model()  # Assuming guests are users


class CarParking(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    opening_hours = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name    
    
class ParkingSpot(models.Model):
    car_parking = models.ForeignKey(CarParking, on_delete=models.CASCADE)
    spot_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Spot {self.spot_number} at {self.car_parking.name}"
 
    
class ParkingBooking(models.Model): 
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    guest = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
      return f"Booking at {self.parking_spot.car_parking.name} on {self.booking_date}"

class ParkingPayment(models.Model):
    parking_booking = models.ForeignKey(ParkingBooking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')])
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.parking_booking} - {self.amount}"
    
class ParkingReview(models.Model):
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    # guest = models.ForeignKey(guest, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.guest.name}'s review for {self.parking_spot.car_parking.name}"
    
class ParkingGalleryImage(models.Model):
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='parking_gallery_images/')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Image for {self.parking_spot.car_parking.name} - {self.title}"
 
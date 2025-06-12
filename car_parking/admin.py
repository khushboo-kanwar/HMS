from django.contrib import admin # type: ignore
from .models import (
    CarParking,
    ParkingSpot,
    ParkingBooking,
    ParkingPayment,
    ParkingReview,
    ParkingGalleryImage
)

@admin.register(CarParking)
class CarParkingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'opening_hours')
    search_fields = ('name', 'address')


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('spot_number', 'car_parking', 'is_available', 'price_per_hour')
    list_filter = ('car_parking', 'is_available')
    search_fields = ('spot_number',)


@admin.register(ParkingBooking)
class ParkingBookingAdmin(admin.ModelAdmin):
    list_display = ('parking_spot', 'guest', 'booking_date', 'start_time', 'end_time')
    list_filter = ('booking_date',)
    search_fields = ('parking_spot__spot_number', 'guest__username')


@admin.register(ParkingPayment)
class ParkingPaymentAdmin(admin.ModelAdmin):
    list_display = ('parking_booking', 'amount', 'payment_method', 'transaction_id', 'payment_date')
    list_filter = ('payment_method', 'payment_date')
    search_fields = ('transaction_id',)


@admin.register(ParkingReview)
class ParkingReviewAdmin(admin.ModelAdmin):
    list_display = ('parking_spot', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('parking_spot__spot_number', 'guest__username')


@admin.register(ParkingGalleryImage)
class ParkingGalleryImageAdmin(admin.ModelAdmin):
    list_display = ('parking_spot', 'title')
    search_fields = ('title', 'parking_spot__spot_number')

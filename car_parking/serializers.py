from events.serializers import EventSerializer
from rest_framework import serializers # type: ignore
from .models import (
    CarParking,
    ParkingSpot,
    ParkingBooking,
    ParkingPayment,
    ParkingReview,
    ParkingGalleryImage
)


class CarParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarParking
        fields = '__all__'


class ParkingSpotSerializer(serializers.ModelSerializer):
    car_parking = CarParkingSerializer(read_only=True)

    class Meta:
        model = ParkingSpot
        fields = '__all__'



class ParkingBookingSerializer(serializers.ModelSerializer):
    parking_spot = ParkingSpotSerializer(read_only=True)
    guest = EventSerializer(read_only=True)

    class Meta:
        model = ParkingBooking
        fields = '__all__'


class ParkingPaymentSerializer(serializers.ModelSerializer):
    parking_booking = ParkingBookingSerializer(read_only=True)

    class Meta:
        model = ParkingPayment
        fields = '__all__'


class ParkingReviewSerializer(serializers.ModelSerializer):
    parking_spot = ParkingSpotSerializer(read_only=True)
    guest = EventSerializer(read_only=True)

    class Meta:
        model = ParkingReview
        fields = '__all__'


class ParkingGalleryImageSerializer(serializers.ModelSerializer):
    parking_spot = ParkingSpotSerializer(read_only=True)

    class Meta:
        model = ParkingGalleryImage
        fields = '__all__'

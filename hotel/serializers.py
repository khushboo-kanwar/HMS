from rest_framework import serializers # type: ignore
from .models import (
    RoomType, Room, Payment, Review, ContactMessage, HotelInfo,
    CheckInRecord, BiometricAttendance, Procurement, POS, FormBuilder,
    CoworkingSpace, Security_Guards, Sports_Club, Locker_and_Safe,
    Garage_and_Workshop, Newspaper, Property_Management, Eldery_Care,
    Hospital, Optical_and_Eye_Care, Medical_Lab, Pharmacy, Beauty_Spa,
    Beverage, Facilities, SupportTicket
)
from users.models import User, Staff

# === Base User Serializer (for references) ===
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'name', 'email', 'position']

# === Room & Booking ===

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = '__all__'



# === Payment, POS, Procurement ===

class PaymentSerializer(serializers.ModelSerializer):
    booking = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = '__all__'

class POSSerializer(serializers.ModelSerializer):
    booking = serializers.StringRelatedField()

    class Meta:
        model = POS
        fields = '__all__'

class ProcurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurement
        fields = '__all__'


# === Review, Contact, Support ===

class ReviewSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    room = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class FormBuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormBuilder
        fields = '__all__'

class SupportTicketSerializer(serializers.ModelSerializer):
    customer = UserSerializer()

    class Meta:
        model = SupportTicket
        fields = '__all__'

class BeautySpaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beauty_Spa
        fields = '__all__'

        
# === Hotel Info ===

class HotelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelInfo
        fields = '__all__'


# === Attendance & CheckIn ===

class CheckInRecordSerializer(serializers.ModelSerializer):
    booking = BookingSerializer() # type: ignore

    class Meta:
        model = CheckInRecord
        fields = '__all__'

class BiometricAttendanceSerializer(serializers.ModelSerializer):
    employee = StaffSerializer()

    class Meta:
        model = BiometricAttendance
        fields = '__all__'


# === Services & Facilities ===

class CoworkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoworkingSpace
        fields = '__all__'

class SportsClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports_Club
        fields = '__all__'

class SecurityGuardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Security_Guards
        fields = '__all__'

class LockerAndSafeSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer()

    class Meta:
        model = Locker_and_Safe
        fields = '__all__'

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = '__all__'

class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = '__all__'


# === Healthcare ===

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class OpticalEyeCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Optical_and_Eye_Care
        fields = '__all__'

class MedicalLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical_Lab
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

class ElderyCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eldery_Care
        fields = '__all__'


# === Real Estate & Media ===

class GarageWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage_and_Workshop
        fields = '__all__'

class PropertyManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_Management
        fields = '__all__'

class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = '__all__'

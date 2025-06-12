from rest_framework import serializers # type: ignore
from .models import User, CustomerProfile, VendorProfile, HotelProfile, StaffProfile, Staff


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'phone', 'address', 'email', 'first_name', 'last_name']

# CustomerProfile Serializer
class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CustomerProfile
        fields = ['user', 'wallet_balance']

# VendorProfile Serializer
class VendorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = VendorProfile
        fields = ['user', 'company_name', 'gst_number']

# HotelProfile Serializer
class HotelProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = HotelProfile
        fields = ['user', 'hotel_name', 'location']

# StaffProfile Serializer
class StaffProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StaffProfile
        fields = ['user', 'position']

# Staff Serializer
class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Staff
        fields = [
            'user', 'role', 'contact', 'img', 'shift_start_time', 'shift_end_time', 
            'emergency_contact', 'email', 'address', 'hire_date', 'salary', 'id_proof'
        ]

# For creating or updating User profiles (optional if needed)
class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role', 'phone', 'address', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# If you need nested profiles while creating/updating user
class CreateCustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['user', 'wallet_balance']

class CreateVendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = ['user', 'company_name', 'gst_number']

class CreateHotelProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelProfile
        fields = ['user', 'hotel_name', 'location']

class CreateStaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = ['user', 'position']

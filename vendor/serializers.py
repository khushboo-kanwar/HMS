from rest_framework import serializers # type: ignore
from .models import Vendor, VendorCategory, VendorService, VendorBooking, Product, Quotation, Project, Sales, Consignment
from users.models import User

# User serializer (assuming a custom User model exists)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# VendorCategory serializer
class VendorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorCategory
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

# Vendor serializer
class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = VendorCategorySerializer(read_only=True)
    
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'name', 'address', 'phone_number', 'email', 'description', 'created_at', 'updated_at', 'category']

# VendorService serializer
class VendorServiceSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = VendorService
        fields = ['id', 'vendor', 'name', 'description', 'price', 'duration', 'is_available']

# VendorBooking serializer
class VendorBookingSerializer(serializers.ModelSerializer):
    vendor_service = VendorServiceSerializer(read_only=True)

    class Meta:
        model = VendorBooking
        fields = ['id', 'vendor_service', 'guest_name', 'guest_email', 'guest_phone', 'booking_date', 'special_requests']

# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'vendor', 'created_at', 'updated_at']

# Quotation serializer
class QuotationSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    customer = UserSerializer(read_only=True)
    service = VendorServiceSerializer(read_only=True)

    class Meta:
        model = Quotation
        fields = ['id', 'vendor', 'customer', 'service', 'message', 'amount', 'created_at', 'is_approved']

# Project serializer
class ProjectSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'vendor', 'title', 'description', 'start_date', 'end_date', 'status', 'created_at']

# Sales serializer
class SalesSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Sales
        fields = ['id', 'vendor', 'product', 'quantity', 'total_price', 'sale_date']

# Consignment serializer
class ConsignmentSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Consignment
        fields = ['id', 'vendor', 'product', 'quantity', 'consignment_date', 'status']

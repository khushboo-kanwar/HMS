from django.contrib import admin # type: ignore
from .models import User, CustomerProfile, VendorProfile, HotelProfile, StaffProfile, Staff

# Custom User Admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'email', 'phone', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_active')

admin.site.register(User, UserAdmin)

# CustomerProfile Admin
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet_balance')

admin.site.register(CustomerProfile, CustomerProfileAdmin)

# VendorProfile Admin
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'gst_number')

admin.site.register(VendorProfile, VendorProfileAdmin)

# HotelProfile Admin
class HotelProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel_name', 'location')

admin.site.register(HotelProfile, HotelProfileAdmin)

# StaffProfile Admin
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position')

admin.site.register(StaffProfile, StaffProfileAdmin)

# Staff Admin
class StaffAdmin(admin.ModelAdmin):
    list_display = ( 'role', 'contact', 'email', 'shift_start_time', 'shift_end_time', 'hire_date', 'salary')
    search_fields = ('user__username', 'role', 'email')
    list_filter = ('role',)

admin.site.register(Staff, StaffAdmin)

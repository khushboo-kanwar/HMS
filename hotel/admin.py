from django.contrib import admin # type: ignore
from .models import (
    RoomType, Room,  Payment, Review, ContactMessage, HotelInfo,
    CheckInRecord, BiometricAttendance, Procurement, POS,
    CoworkingSpace, Security_Guards, Sports_Club, Locker_and_Safe,
    Garage_and_Workshop, Newspaper, Property_Management, Eldery_Care,
    Hospital, Optical_and_Eye_Care, Medical_Lab, Pharmacy, Beauty_Spa,
     Beverage, Facilities, Suport_Ticket
)
from .models import From_Builder

# === Room & Booking ===

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_night', 'max_occupancy')
    search_fields = ('name',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'floor', 'status', 'is_available')
    list_filter = ('status', 'floor', 'room_type')
    search_fields = ('room_number',)

# === Reviews, Contact, Hotel ===

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'room', 'rating', 'created_at')
    search_fields = ('customer__name', 'room__room_number')
    list_filter = ('rating',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('name', 'email')

@admin.register(HotelInfo)
class HotelInfoAdmin(admin.ModelAdmin):
    list_display = ('location', 'contact_email', 'phone')


# === Staff & Attendance ===

@admin.register(CheckInRecord)
class CheckInRecordAdmin(admin.ModelAdmin):
    list_display = ('booking', 'check_in_time', 'check_out_time', 'is_active')

@admin.register(BiometricAttendance)
class BiometricAttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in_time', 'check_out_time')
    list_filter = ('employee', 'date')

@admin.register(Security_Guards)
class SecurityGuardsAdmin(admin.ModelAdmin):
    list_display = ('name', 'assigned_area', 'shift_start_time', 'shift_end_time')


# === Financial ===

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_method', 'payment_date')
    search_fields = ('transaction_id',)

@admin.register(POS)
class POSAdmin(admin.ModelAdmin):
    list_display = ('booking', 'total_amount', 'payment_status', 'payment_date')
    list_filter = ('payment_status',)

@admin.register(Procurement)
class ProcurementAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'supplier', 'order_date', 'total_cost')
    search_fields = ('item_name', 'supplier')


# === Communication ===
class From_BuilderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at', 'is_read')
    search_fields = ('name', 'email')
    list_filter = ('is_read',)

admin.site.register(From_Builder, From_BuilderAdmin)


@admin.register(Suport_Ticket)
class SuportTicketAdmin(admin.ModelAdmin):
    list_display = ('customer', 'subject', 'status', 'created_at')
    search_fields = ('customer__name', 'subject')
    list_filter = ('status',)


# === Services & Amenities ===

admin.site.register(CoworkingSpace)
admin.site.register(Sports_Club)
admin.site.register(Beauty_Spa)
admin.site.register(Facilities)
admin.site.register(Locker_and_Safe)
admin.site.register(Beverage)
admin.site.register(Newspaper)


# === Healthcare ===

admin.site.register(Hospital)
admin.site.register(Optical_and_Eye_Care)
admin.site.register(Medical_Lab)
admin.site.register(Pharmacy)
admin.site.register(Eldery_Care)


# === Real Estate ===

admin.site.register(Garage_and_Workshop)
admin.site.register(Property_Management)

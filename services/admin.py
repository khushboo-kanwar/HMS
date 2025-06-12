from django.contrib import admin # type: ignore
from .models import (
    ServiceCategory, Service, ServiceBooking, ServicePayment, ServiceReview,
    SocialMedia, ContactMessage, RoomCleaningLog, Offer, Recruitment, Job_search,
    Movie_and_TV, Movie_show_booking, Water_park, GYM_management, Constriction,
    Fleet, Vehicle_Trade, Vehicle_booking, Car_Dealership, Tailoring_and_Fashion_design,
    Dairy_Cattle, Mobile_Service, Vehicle_Inspection, Machine_Repair, Repair, AI,
    Catering, Rental, Sales_Agent, Sales_Force, Contract, Documents, Google_Docs,
    Custom_Field, Queue_Management, Game_Zone, Video_Hub, Photo_and_Studio,
    File_Sharing, Feedback, Newsletter
)

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name',)

@admin.register(ServiceBooking)
class ServiceBookingAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'service', 'booking_date',)
    search_fields = ('guest_name', 'service__name')

@admin.register(ServicePayment)
class ServicePaymentAdmin(admin.ModelAdmin):
    list_display = ('service_booking', 'amount', 'payment_method', 'payment_date')
    list_filter = ('payment_method',)
    search_fields = ('service_booking__guest_name',)

@admin.register(ServiceReview)
class ServiceReviewAdmin(admin.ModelAdmin):
    list_display = ('service', 'guest_name', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('guest_name', 'service__name')

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_visible')
    search_fields = ('name',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'created_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('guest_name',)

@admin.register(RoomCleaningLog)
class RoomCleaningLogAdmin(admin.ModelAdmin):
    list_display = ('room', 'cleaned_by', 'cleaned_at')
    list_filter = ('cleaned_by',)
    search_fields = ('room__room_number', 'cleaned_by__name')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'percentage', 'valid_from', 'valid_to', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'code')

@admin.register(Recruitment)
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'application_deadline', 'is_open')
    list_filter = ('is_open',)
    search_fields = ('title',)

@admin.register(Job_search)
class JobSearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'application_deadline', 'is_open')
    list_filter = ('is_open',)
    search_fields = ('title',)

@admin.register(Movie_and_TV)
class MovieAndTVAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'genre', 'rating')
    list_filter = ('genre',)
    search_fields = ('title',)

@admin.register(Movie_show_booking)
class MovieShowBookingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'guest_name', 'booking_date')
    search_fields = ('guest_name', 'movie__title')

@admin.register(Water_park)
class WaterParkAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'opening_hours', 'ticket_price', 'is_open')
    list_filter = ('is_open',)
    search_fields = ('title', 'location')

@admin.register(GYM_management)
class GymManagementAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'opening_hours', 'membership_fee', 'is_open')
    list_filter = ('is_open',)
    search_fields = ('title', 'location')

@admin.register(Constriction)
class ConstrictionAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'project_cost')
    search_fields = ('title', 'location')

@admin.register(Fleet)
class FleetAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'license_plate', 'capacity', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('vehicle_type', 'license_plate')

@admin.register(Vehicle_Trade)
class VehicleTradeAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'trade_type', 'trade_date', 'amount')
    list_filter = ('trade_type',)
    search_fields = ('vehicle__license_plate',)

@admin.register(Vehicle_booking)
class VehicleBookingAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'guest_name', 'booking_date')
    search_fields = ('guest_name', 'vehicle__license_plate')

@admin.register(Car_Dealership)
class CarDealershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_number', 'email')
    search_fields = ('name', 'location')

@admin.register(Tailoring_and_Fashion_design)
class TailoringAndFashionDesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'opening_hours', 'service_fee')
    search_fields = ('title',)

@admin.register(Dairy_Cattle)
class DairyCattleAdmin(admin.ModelAdmin):
    list_display = ('breed', 'age', 'weight', 'health_status', 'is_available_for_sale')
    list_filter = ('is_available_for_sale',)
    search_fields = ('breed',)

@admin.register(Mobile_Service)
class MobileServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('service_type',)

@admin.register(Vehicle_Inspection)
class VehicleInspectionAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'inspection_date', 'inspector_name')
    search_fields = ('vehicle__license_plate', 'inspector_name')

@admin.register(Machine_Repair)
class MachineRepairAdmin(admin.ModelAdmin):
    list_display = ('machine_type', 'repair_date', 'cost')
    search_fields = ('machine_type',)

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'repair_date', 'cost')
 

from django.contrib import admin # type: ignore
from .models import Vendor, VendorCategory, VendorService, VendorBooking, Product, Quotation, Project, Sales, Consignment

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'updated_at')

class VendorServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor', 'price', 'duration', 'is_available')
    search_fields = ('name', 'vendor__name')
    list_filter = ('is_available', 'vendor')

class VendorBookingAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'vendor_service', 'guest_email', 'booking_date', 'special_requests')
    search_fields = ('guest_name', 'guest_email', 'vendor_service__name')
    list_filter = ('booking_date', 'vendor_service')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'vendor__name')
    list_filter = ('created_at', 'vendor')

class QuotationAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'customer', 'service', 'amount', 'created_at', 'is_approved')
    search_fields = ('vendor__name', 'customer__username', 'service__name')
    list_filter = ('is_approved', 'created_at')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'vendor', 'start_date', 'end_date', 'status', 'created_at')
    search_fields = ('title', 'vendor__name', 'status')
    list_filter = ('status', 'start_date', 'end_date')

class SalesAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'product', 'quantity', 'total_price', 'sale_date')
    search_fields = ('vendor__name', 'product__name')
    list_filter = ('sale_date', 'vendor')

class ConsignmentAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'product', 'quantity', 'consignment_date', 'status')
    search_fields = ('vendor__name', 'product__name')
    list_filter = ('status', 'consignment_date')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorCategory)
admin.site.register(VendorService, VendorServiceAdmin)
admin.site.register(VendorBooking, VendorBookingAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Quotation, QuotationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Consignment, ConsignmentAdmin)

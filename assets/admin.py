from django.contrib import admin # type: ignore
from .models import (
    AssetCategory,
    Asset,
    Proposal,
    Rtainer,
    Invoice,
    Purchase,
    CMMS,
    School_and_Institute,
    Music_Institute,
    Childcare,
    Driving_School,
    Waste_Management,
    Fix_Equipment,
    HubSpot,
)

@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'status', 'value')

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('asset', 'proposal_date', 'proposed_value', 'status')

@admin.register(Rtainer)
class RtainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'created_at')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('amount', 'invoice_date', 'due_date', 'status')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('asset', 'purchase_price', 'supplier', 'purchase_date')

@admin.register(CMMS)
class CMMSAdmin(admin.ModelAdmin):
    list_display = ('asset', 'maintenance_date', 'maintenance_type', 'cost')

@admin.register(School_and_Institute)
class SchoolAndInstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')

@admin.register(Music_Institute)
class MusicInstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')

@admin.register(Childcare)
class ChildcareAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')

@admin.register(Driving_School)
class DrivingSchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')

@admin.register(Waste_Management)
class WasteManagementAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')

@admin.register(Fix_Equipment)
class FixedEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')

@admin.register(HubSpot)
class HubSpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')

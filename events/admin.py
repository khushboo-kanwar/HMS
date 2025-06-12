from django.contrib import admin # type: ignore
from .models import (
    EventCategory, Event, EventBooking, EventPayment, EventReview,
    EventGalleryImage, EventService, EventOffer, EventContactMessage,
    EventManagement, Insurance, Courier, Frieght, Calendar, Outlook_Calendar,
    Zoom_Meeting, Google_Meet, Whereby_Meeting, Zoho_Meeting, Livestrom_Meeting,
    Goto_Meeting, Meeting_Hub, Apoitment, Portfolio, Resume_Builder, Reminder,
    Workflow, Google_Sheet, Spreadsheet, Find_Google_Leads
)

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'organizer_name')
    search_fields = ('name', 'organizer_name')
    list_filter = ('date',)

@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'guest_name', 'booking_date', 'number_of_guests')
    search_fields = ('guest_name', 'guest_email')
    list_filter = ('booking_date',)

@admin.register(EventPayment)
class EventPaymentAdmin(admin.ModelAdmin):
    list_display = ('event_booking', 'amount', 'payment_method', 'payment_date')
    search_fields = ('transaction_id',)

@admin.register(EventReview)
class EventReviewAdmin(admin.ModelAdmin):
    list_display = ('event', 'guest_name', 'rating', 'created_at')
    list_filter = ('rating',)

@admin.register(EventGalleryImage)
class EventGalleryImageAdmin(admin.ModelAdmin):
    list_display = ('event', 'title', 'is_visible', 'uploaded_at')
    list_filter = ('is_visible',)

@admin.register(EventService)
class EventServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')

@admin.register(EventOffer)
class EventOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'percentage', 'valid_from', 'valid_to', 'is_active')
    list_filter = ('is_active',)

@admin.register(EventContactMessage)
class EventContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    search_fields = ('name', 'email')

@admin.register(EventManagement)
class EventManagementAdmin(admin.ModelAdmin):
    list_display = ('event', 'manager_name', 'assigned_at')

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'provider_name', 'coverage_amount', 'start_date', 'end_date')

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_price', 'service_duration')

@admin.register(Frieght)
class FrieghtAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_price', 'service_duration')

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'time')

@admin.register(Outlook_Calendar)
class OutlookCalendarAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'time')

@admin.register(Zoom_Meeting)
class ZoomMeetingAdmin(admin.ModelAdmin):
    list_display = ('event', 'meeting_id', 'meeting_date')

@admin.register(Google_Meet)
class GoogleMeetAdmin(admin.ModelAdmin):
    list_display = ('event', 'meeting_id', 'meeting_date')

@admin.register(Whereby_Meeting)
class WherebyMeetingAdmin(admin.ModelAdmin):
    list_display = ('event', 'meeting_id', 'meeting_date')

@admin.register(Zoho_Meeting)
class ZohoMeetingAdmin(admin.ModelAdmin):
    list_display = ('event', 'meeting_id', 'meeting_date')

@admin.register(Livestrom_Meeting)
class LivestromMeetingAdmin(admin.ModelAdmin):
    list_display = ('event', 'meeting_id', 'meeting_date')

@admin.register(Goto_Meeting)
class GotoMeetingAdmin(admin.ModelAdmin):
    list_display = ('event', 'meeting_id', 'meeting_date')

@admin.register(Meeting_Hub)
class MeetingHubAdmin(admin.ModelAdmin):
    list_display = ('event', 'meeting_id', 'meeting_date')

@admin.register(Apoitment)
class ApoitmentAdmin(admin.ModelAdmin):
    list_display = ('event', 'appointment_date', 'appointment_time')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('event', 'portfolio_name', 'created_at')

@admin.register(Resume_Builder)
class ResumeBuilderAdmin(admin.ModelAdmin):
    list_display = ('event', 'resume_name', 'created_at')

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('event', 'reminder_date')

@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('event', 'workflow_name', 'created_at')

@admin.register(Google_Sheet)
class GoogleSheetAdmin(admin.ModelAdmin):
    list_display = ('event', 'sheet_name', 'created_at')

@admin.register(Spreadsheet)
class SpreadsheetAdmin(admin.ModelAdmin):
    list_display = ('event', 'spreadsheet_name', 'created_at')

@admin.register(Find_Google_Leads)
class FindGoogleLeadsAdmin(admin.ModelAdmin):
    list_display = ('lead_name', 'lead_email', 'lead_source', 'created_at')

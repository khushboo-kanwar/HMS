from rest_framework import serializers # type: ignore
from .models import (
    EventCategory, Event, EventBooking, EventPayment, EventReview,
    EventGalleryImage, EventService, EventOffer, EventContactMessage,
    EventManagement, Insurance, Courier, Frieght, Calendar, Outlook_Calendar,
    Zoom_Meeting, Google_Meet, Whereby_Meeting, Zoho_Meeting, Livestrom_Meeting,
    Goto_Meeting, Meeting_Hub, Apoitment, Portfolio, Resume_Builder, Reminder,
    Workflow, Google_Sheet, Spreadsheet, Find_Google_Leads
)

# Serializers for models

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class EventSerializer(serializers.ModelSerializer):
    event_category = EventCategorySerializer()  # Nested serializer example

    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'location', 'description', 'organizer_name', 
                  'organizer_email', 'organizer_phone', 'special_requests']

class EventBookingSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = EventBooking
        fields = ['id', 'event', 'guest_name', 'guest_email', 'guest_phone', 
                  'number_of_guests', 'booking_date', 'special_requests']

class EventPaymentSerializer(serializers.ModelSerializer):
    event_booking = EventBookingSerializer()  # Nested serializer example

    class Meta:
        model = EventPayment
        fields = ['id', 'event_booking', 'amount', 'payment_method', 
                  'transaction_id', 'payment_date']

class EventReviewSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = EventReview
        fields = ['id', 'event', 'guest_name', 'rating', 'comment', 'created_at', 'updated_at']

class EventGalleryImageSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = EventGalleryImage
        fields = ['id', 'event', 'title', 'image', 'uploaded_at', 'is_visible']

class EventServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventService
        fields = ['id', 'name', 'description', 'price', 'icon', 'is_available']

class EventOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventOffer
        fields = ['id', 'title', 'code', 'description', 'percentage', 
                  'valid_from', 'valid_to', 'is_active']

class EventContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventContactMessage
        fields = ['id', 'name', 'email', 'phone', 'message', 'sent_at']

class EventManagementSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = EventManagement
        fields = ['id', 'event', 'manager_name', 'manager_email', 'manager_phone', 'assigned_at']

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['id', 'policy_number', 'provider_name', 'coverage_amount', 
                  'start_date', 'end_date']

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['id', 'service_name', 'service_description', 'service_price', 'service_duration']

class FrieghtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frieght
        fields = ['id', 'service_name', 'service_description', 'service_price', 'service_duration']

class CalendarSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Calendar
        fields = ['id', 'event', 'date', 'time', 'description']

class OutlookCalendarSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Outlook_Calendar
        fields = ['id', 'event', 'date', 'time', 'description']

class ZoomMeetingSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Zoom_Meeting
        fields = ['id', 'event', 'meeting_id', 'meeting_password', 
                  'meeting_date', 'meeting_duration']

class GoogleMeetSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Google_Meet
        fields = ['id', 'event', 'meeting_id', 'meeting_password', 
                  'meeting_date', 'meeting_duration']
        
class WherebyMeetingSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Whereby_Meeting
        fields = ['id', 'event', 'meeting_id', 'meeting_password', 
                  'meeting_date', 'meeting_duration']
class ZohoMeetingSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Zoho_Meeting
        fields = ['id', 'event', 'meeting_id', 'meeting_password', 
                  'meeting_date', 'meeting_duration']
        
class LivestromMeetingSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Livestrom_Meeting
        fields = ['id', 'event', 'meeting_id', 'meeting_password', 
                  'meeting_date', 'meeting_duration']
class GotoMeetingSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Goto_Meeting
        fields = ['id', 'event', 'meeting_id', 'meeting_password', 
                  'meeting_date', 'meeting_duration']
class MeetingHubSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Meeting_Hub
        fields = ['id', 'event', 'meeting_id', 'meeting_password', 
                  'meeting_date', 'meeting_duration']
class AppointmentSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Apoitment
        fields = ['id', 'event', 'appointment_date', 'appointment_time', 
                  'appointment_description']
class PortfolioSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Portfolio
        fields = ['id', 'event', 'portfolio_name', 'portfolio_description', 
                  'created_at', 'updated_at']
class ResumeBuilderSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Resume_Builder
        fields = ['id', 'event', 'resume_name', 'resume_description', 
                  'created_at', 'updated_at']
        

class ReminderSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Reminder
        fields = ['id', 'event', 'reminder_date', 'reminder_message']

class WorkflowSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Workflow
        fields = ['id', 'event', 'workflow_name', 'workflow_description', 'created_at']

class GoogleSheetSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Google_Sheet
        fields = ['id', 'event', 'sheet_name', 'sheet_url', 'created_at']

class SpreadsheetSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Spreadsheet
        fields = ['id', 'event', 'spreadsheet_name', 'spreadsheet_url', 'created_at']

class FindGoogleLeadsSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Nested serializer example

    class Meta:
        model = Find_Google_Leads
        fields = ['id', 'event', 'lead_name', 'lead_email', 'lead_phone', 
                  'lead_source', 'created_at']

from rest_framework import serializers # type: ignore
from .models import (
    ServiceCategory, Service, ServiceBooking, ServicePayment, ServiceReview,
    SocialMedia, ContactMessage, RoomCleaningLog, Offer, Recruitment, Job_search,
    Movie_and_TV, Movie_show_booking, Water_park, GYM_management, Constriction,
    Fleet, Vehicle_Trade, Vehicle_booking, Car_Dealership, Tailoring_and_Fashion_design,
    Dairy_Cattle, Mobile_Service, Vehicle_Inspection, Repair, AI, Catering, Rental,
    Sales_Agent, Sales_Force, Contract, Documents, Google_Docs, Custom_Field,
    Queue_Management, Game_Zone, Video_Hub, Photo_and_Studio, File_Sharing, Feedback,
    Newsletter
)

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBooking
        fields = '__all__'

class ServicePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePayment
        fields = '__all__'

class ServiceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceReview
        fields = '__all__'

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class RoomCleaningLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCleaningLog
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'

class JobSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_search
        fields = '__all__'

class MovieAndTVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_and_TV
        fields = '__all__'

class MovieShowBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_show_booking
        fields = '__all__'

class WaterParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water_park
        fields = '__all__'

class GymManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = GYM_management
        fields = '__all__'

class ConstrictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constriction
        fields = '__all__'

class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fleet
        fields = '__all__'

class VehicleTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Trade
        fields = '__all__'

class VehicleBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_booking
        fields = '__all__'

class CarDealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Dealership
        fields = '__all__'

class TailoringAndFashionDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tailoring_and_Fashion_design
        fields = '__all__'

class DairyCattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy_Cattle
        fields = '__all__'

class MobileServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile_Service
        fields = '__all__'

class VehicleInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Inspection
        fields = '__all__'

class RepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = '__all__'

class AI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AI
        fields = '__all__'

class CateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

class SalesAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales_Agent
        fields = '__all__'

class SalesForceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales_Force
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

class GoogleDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Google_Docs
        fields = '__all__'

class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_Field
        fields = '__all__'

class QueueManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue_Management
        fields = '__all__'

class GameZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Zone
        fields = '__all__'

class VideoHubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_Hub
        fields = '__all__'

class PhotoAndStudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo_and_Studio
        fields = '__all__'

class FileSharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = File_Sharing
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'

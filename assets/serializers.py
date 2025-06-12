from rest_framework import serializers # type: ignore
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

class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'

class RtainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rtainer
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class CMMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMMS
        fields = '__all__'

class SchoolAndInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_and_Institute
        fields = '__all__'

class MusicInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music_Institute
        fields = '__all__'

class ChildcareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Childcare
        fields = '__all__'

class DrivingSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driving_School
        fields = '__all__'

class WasteManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste_Management
        fields = '__all__'

class FixedEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fix_Equipment
        fields = '__all__'

class HubSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = HubSpot
        fields = '__all__'

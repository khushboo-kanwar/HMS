from rest_framework import serializers  # type: ignore
from .models import *

# Generic serializer for models with common fields
class DefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # to be overridden when used
        fields = '__all__'

# Specific serializers (in case you want to customize further later)
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # returns username instead of ID

    class Meta:
        model = Blog
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class GallaryimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallaryimage
        fields = '__all__'

class LegalCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legal_Case
        fields = '__all__'

# Auto-generate serializers for all simple models using DefaultSerializer
# List of simple models to reduce boilerplate
simple_models = [
    HomePage, Aboutus, HRM, CRM, Whatsapp, Instagram, Facebook, Facebook_Post,
    Instagram_Post, Zulip, Youtube, Vcard, LMS, Garden_management, Rotas,
    Commision, Agriculture, Tour_and_Travel, Woo_Commerce, Shopify, Indiamart,
    Sage, Asana, Inventory, Request, Inovation_Center, Business_Mapping,
    RoadMap_Central, Planning, Internal_Knowledge, Call_Hub, Email_Box,
    Sendinblue, Side_Menu_Builder, Activity_Log, OneNote, Notes, Team_Workload,
    Quiz_Management, Petty_Cash, Trello, To_Do, Time_Tracker, Timesheet,
    Messenger, Visitors, Api_Docs, Helpdesk, Setup_Subscription_plan, Settings,
]

# Dynamically create serializer classes for simple models
for model in simple_models:
    serializer_class = type(
        f"{model.__name__}Serializer",
        (serializers.ModelSerializer,),
        {
            'Meta': type('Meta', (), {
                'model': model,
                'fields': '__all__'
            })
        }
    )
    globals()[serializer_class.__name__] = serializer_class

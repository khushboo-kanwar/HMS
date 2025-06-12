# views.py
from rest_framework import status  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response # type: ignore
from drf_yasg.utils import swagger_auto_schema # type: ignore
from .models import (
    Page, Blog, MediaFile, HomePage, Aboutus, Gallaryimage, SocialMedia,
    ContactMessage, HRM, CRM, Whatsapp, Instagram, Facebook, Facebook_Post,     
    Instagram_Post, Zulip, Youtube, Vcard, LMS, Garden_management, Rotas,
    Commision, Agriculture, Legal_Case, Tour_and_Travel, Woo_Commerce, Shopify,
    Indiamart, Sage, Asana, Inventory, Request, Inovation_Center, Business_Mapping,
    RoadMap_Central, Planning, Internal_Knowledge, Call_Hub, Email_Box, Sendinblue,
    Side_Menu_Builder, Activity_Log, OneNote, Notes, Team_Workload, Quiz_Management,
    Petty_Cash, Trello, To_Do, Time_Tracker, Timesheet, Messenger, Visitors, Api_Docs,
    Helpdesk, Setup_Subscription_plan, Settings
)
from .serializers import (
    PageSerializer, BlogSerializer, MediaFileSerializer, HomePageSerializer,
    AboutusSerializer, GallaryimageSerializer, SocialMediaSerializer,
    ContactMessageSerializer, HRMSerializer, CRMSerializer, WhatsappSerializer,
    InstagramSerializer, FacebookSerializer, Facebook_PostSerializer,
    Instagram_PostSerializer, ZulipSerializer, YoutubeSerializer, VcardSerializer,
    LMSSerializer, Garden_managementSerializer, RotasSerializer, CommisionSerializer,
    AgricultureSerializer, Legal_CaseSerializer, Tour_and_TravelSerializer,
    Woo_CommerceSerializer, ShopifySerializer, IndiamartSerializer, SageSerializer,
    AsanaSerializer, InventorySerializer, RequestSerializer, Inovation_CenterSerializer,
    Business_MappingSerializer, RoadMap_CentralSerializer, PlanningSerializer,
    Internal_KnowledgeSerializer, Call_HubSerializer, Email_BoxSerializer,
    SendinblueSerializer, Side_Menu_BuilderSerializer, Activity_LogSerializer,
    OneNoteSerializer, NotesSerializer, Team_WorkloadSerializer, Quiz_ManagementSerializer,
    Petty_CashSerializer, TrelloSerializer, To_DoSerializer, Time_TrackerSerializer,
    TimesheetSerializer, MessengerSerializer, VisitorsSerializer, Api_DocsSerializer,
    HelpdeskSerializer, Setup_Subscription_planSerializer, SettingsSerializer
)

class PageListCreateView(APIView):
    @swagger_auto_schema(responses={200: PageSerializer(many=True)})
    def get(self, request):
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PageSerializer)
    def post(self, request):
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PageDetailView(APIView):
    @swagger_auto_schema(responses={200: PageSerializer})
    def get(self, request, pk):
        try:
            page = Page.objects.get(pk=pk)
            serializer = PageSerializer(page)
            return Response(serializer.data)
        except Page.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=PageSerializer)
    def put(self, request, pk):
        try:
            page = Page.objects.get(pk=pk)
            serializer = PageSerializer(page, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Page.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            page = Page.objects.get(pk=pk)
            page.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Page.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class BlogListCreateView(APIView):
    @swagger_auto_schema(responses={200: BlogSerializer(many=True)})
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BlogSerializer)
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailView(APIView):
    @swagger_auto_schema(responses={200: BlogSerializer})
    def get(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=BlogSerializer)
    def put(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            serializer = BlogSerializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class MediaFileListCreateView(APIView):
    @swagger_auto_schema(responses={200: MediaFileSerializer(many=True)})
    def get(self, request):
        media_files = MediaFile.objects.all()
        serializer = MediaFileSerializer(media_files, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MediaFileSerializer)
    def post(self, request):
        serializer = MediaFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MediaFileDetailView(APIView):
    @swagger_auto_schema(responses={200: MediaFileSerializer})
    def get(self, request, pk):
        try:
            media_file = MediaFile.objects.get(pk=pk)
            serializer = MediaFileSerializer(media_file)
            return Response(serializer.data)
        except MediaFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=MediaFileSerializer)
    def put(self, request, pk):
        try:
            media_file = MediaFile.objects.get(pk=pk)
            serializer = MediaFileSerializer(media_file, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MediaFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            media_file = MediaFile.objects.get(pk=pk)
            media_file.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MediaFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class HomePageListCreateView(APIView):
    @swagger_auto_schema(responses={200: HomePageSerializer(many=True)})
    def get(self, request):
        home_pages = HomePage.objects.all()
        serializer = HomePageSerializer(home_pages, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=HomePageSerializer)
    def post(self, request):
        serializer = HomePageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HomePageDetailView(APIView):
    @swagger_auto_schema(responses={200: HomePageSerializer})
    def get(self, request, pk):
        try:
            home_page = HomePage.objects.get(pk=pk)
            serializer = HomePageSerializer(home_page)
            return Response(serializer.data)
        except HomePage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=HomePageSerializer)
    def put(self, request, pk):
        try:
            home_page = HomePage.objects.get(pk=pk)
            serializer = HomePageSerializer(home_page, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except HomePage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            home_page = HomePage.objects.get(pk=pk)
            home_page.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except HomePage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class AboutusListCreateView(APIView):
    @swagger_auto_schema(responses={200: AboutusSerializer(many=True)})
    def get(self, request):
        aboutus = Aboutus.objects.all()
        serializer = AboutusSerializer(aboutus, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AboutusSerializer)
    def post(self, request):
        serializer = AboutusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AboutusDetailView(APIView):   
    @swagger_auto_schema(responses={200: AboutusSerializer})
    def get(self, request, pk):
        try:
            aboutus = Aboutus.objects.get(pk=pk)
            serializer = AboutusSerializer(aboutus)
            return Response(serializer.data)
        except Aboutus.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=AboutusSerializer)
    def put(self, request, pk):
        try:
            aboutus = Aboutus.objects.get(pk=pk)
            serializer = AboutusSerializer(aboutus, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Aboutus.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            aboutus = Aboutus.objects.get(pk=pk)
            aboutus.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Aboutus.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class GallaryimageListCreateView(APIView):  
    @swagger_auto_schema(responses={200: GallaryimageSerializer(many=True)})
    def get(self, request):
        gallaryimages = Gallaryimage.objects.all()
        serializer = GallaryimageSerializer(gallaryimages, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GallaryimageSerializer)
    def post(self, request):
        serializer = GallaryimageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GallaryimageDetailView(APIView):  
    @swagger_auto_schema(responses={200: GallaryimageSerializer})
    def get(self, request, pk):
        try:
            gallaryimage = Gallaryimage.objects.get(pk=pk)
            serializer = GallaryimageSerializer(gallaryimage)
            return Response(serializer.data)
        except Gallaryimage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=GallaryimageSerializer)
    def put(self, request, pk):
        try:
            gallaryimage = Gallaryimage.objects.get(pk=pk)
            serializer = GallaryimageSerializer(gallaryimage, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Gallaryimage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            gallaryimage = Gallaryimage.objects.get(pk=pk)
            gallaryimage.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Gallaryimage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class SocialMediaListCreateView(APIView):
    @swagger_auto_schema(responses={200: SocialMediaSerializer(many=True)})
    def get(self, request):
        social_media = SocialMedia.objects.all()
        serializer = SocialMediaSerializer(social_media, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SocialMediaSerializer)
    def post(self, request):
        serializer = SocialMediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SocialMediaDetailView(APIView):   
    @swagger_auto_schema(responses={200: SocialMediaSerializer})
    def get(self, request, pk):
        try:
            social_media = SocialMedia.objects.get(pk=pk)
            serializer = SocialMediaSerializer(social_media)
            return Response(serializer.data)
        except SocialMedia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=SocialMediaSerializer)
    def put(self, request, pk):
        try:
            social_media = SocialMedia.objects.get(pk=pk)
            serializer = SocialMediaSerializer(social_media, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SocialMedia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            social_media = SocialMedia.objects.get(pk=pk)
            social_media.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SocialMedia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class ContactMessageListCreateView(APIView):
    @swagger_auto_schema(responses={200: ContactMessageSerializer(many=True)})
    def get(self, request):
        contact_messages = ContactMessage.objects.all()
        serializer = ContactMessageSerializer(contact_messages, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContactMessageSerializer)
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ContactMessageDetailView(APIView):    
    @swagger_auto_schema(responses={200: ContactMessageSerializer})
    def get(self, request, pk):
        try:
            contact_message = ContactMessage.objects.get(pk=pk)
            serializer = ContactMessageSerializer(contact_message)
            return Response(serializer.data)
        except ContactMessage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=ContactMessageSerializer)
    def put(self, request, pk):
        try:
            contact_message = ContactMessage.objects.get(pk=pk)
            serializer = ContactMessageSerializer(contact_message, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ContactMessage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            contact_message = ContactMessage.objects.get(pk=pk)
            contact_message.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ContactMessage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class HRMListCreateView(APIView):   
    @swagger_auto_schema(responses={200: HRMSerializer(many=True)})
    def get(self, request):
        hrm = HRM.objects.all()
        serializer = HRMSerializer(hrm, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=HRMSerializer)
    def post(self, request):
        serializer = HRMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HRMDetailView(APIView):
    @swagger_auto_schema(responses={200: HRMSerializer})
    def get(self, request, pk):
        try:
            hrm = HRM.objects.get(pk=pk)
            serializer = HRMSerializer(hrm)
            return Response(serializer.data)
        except HRM.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=HRMSerializer)
    def put(self, request, pk):
        try:
            hrm = HRM.objects.get(pk=pk)
            serializer = HRMSerializer(hrm, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except HRM.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            hrm = HRM.objects.get(pk=pk)
            hrm.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except HRM.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class CRMListCreateView(APIView):
    @swagger_auto_schema(responses={200: CRMSerializer(many=True)})
    def get(self, request):
        crm = CRM.objects.all()
        serializer = CRMSerializer(crm, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CRMSerializer)
    def post(self, request):
        serializer = CRMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CRMDetailView(APIView):
    @swagger_auto_schema(responses={200: CRMSerializer})
    def get(self, request, pk):
        try:
            crm = CRM.objects.get(pk=pk)
            serializer = CRMSerializer(crm)
            return Response(serializer.data)
        except CRM.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=CRMSerializer)
    def put(self, request, pk):
        try:
            crm = CRM.objects.get(pk=pk)
            serializer = CRMSerializer(crm, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CRM.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            crm = CRM.objects.get(pk=pk)
            crm.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CRM.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class WhatsappListCreateView(APIView):
    @swagger_auto_schema(responses={200: WhatsappSerializer(many=True)})
    def get(self, request):
        whatsapp = Whatsapp.objects.all()
        serializer = WhatsappSerializer(whatsapp, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=WhatsappSerializer)
    def post(self, request):
        serializer = WhatsappSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class WhatsappDetailView(APIView):
    @swagger_auto_schema(responses={200: WhatsappSerializer})
    def get(self, request, pk):
        try:
            whatsapp = Whatsapp.objects.get(pk=pk)
            serializer = WhatsappSerializer(whatsapp)
            return Response(serializer.data)
        except Whatsapp.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=WhatsappSerializer)
    def put(self, request, pk):
        try:
            whatsapp = Whatsapp.objects.get(pk=pk)
            serializer = WhatsappSerializer(whatsapp, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Whatsapp.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            whatsapp = Whatsapp.objects.get(pk=pk)
            whatsapp.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Whatsapp.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class InstagramListCreateView(APIView):
    @swagger_auto_schema(responses={200: InstagramSerializer(many=True)})
    def get(self, request):
        instagram = Instagram.objects.all()
        serializer = InstagramSerializer(instagram, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=InstagramSerializer)
    def post(self, request):
        serializer = InstagramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class InstagramDetailView(APIView):
    @swagger_auto_schema(responses={200: InstagramSerializer})
    def get(self, request, pk):
        try:
            instagram = Instagram.objects.get(pk=pk)
            serializer = InstagramSerializer(instagram)
            return Response(serializer.data)
        except Instagram.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=InstagramSerializer)
    def put(self, request, pk):
        try:
            instagram = Instagram.objects.get(pk=pk)
            serializer = InstagramSerializer(instagram, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Instagram.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            instagram = Instagram.objects.get(pk=pk)
            instagram.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Instagram.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class FacebookListCreateView(APIView):
    @swagger_auto_schema(responses={200: FacebookSerializer(many=True)})
    def get(self, request):
        facebook = Facebook.objects.all()
        serializer = FacebookSerializer(facebook, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=FacebookSerializer)
    def post(self, request):
        serializer = FacebookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class FacebookDetailView(APIView):
    @swagger_auto_schema(responses={200: FacebookSerializer})
    def get(self, request, pk):
        try:
            facebook = Facebook.objects.get(pk=pk)
            serializer = FacebookSerializer(facebook)
            return Response(serializer.data)
        except Facebook.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=FacebookSerializer)
    def put(self, request, pk):
        try:
            facebook = Facebook.objects.get(pk=pk)
            serializer = FacebookSerializer(facebook, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Facebook.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            facebook = Facebook.objects.get(pk=pk)
            facebook.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Facebook.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Facebook_PostListCreateView(APIView):
    @swagger_auto_schema(responses={200: Facebook_PostSerializer(many=True)})
    def get(self, request):
        facebook_posts = Facebook_Post.objects.all()
        serializer = Facebook_PostSerializer(facebook_posts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Facebook_PostSerializer)
    def post(self, request):
        serializer = Facebook_PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Facebook_PostDetailView(APIView):
    @swagger_auto_schema(responses={200: Facebook_PostSerializer})
    def get(self, request, pk):
        try:
            facebook_post = Facebook_Post.objects.get(pk=pk)
            serializer = Facebook_PostSerializer(facebook_post)
            return Response(serializer.data)
        except Facebook_Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Facebook_PostSerializer)
    def put(self, request, pk):
        try:
            facebook_post = Facebook_Post.objects.get(pk=pk)
            serializer = Facebook_PostSerializer(facebook_post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Facebook_Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            facebook_post = Facebook_Post.objects.get(pk=pk)
            facebook_post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Facebook_Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Instagram_PostListCreateView(APIView):
    @swagger_auto_schema(responses={200: Instagram_PostSerializer(many=True)})
    def get(self, request):
        instagram_posts = Instagram_Post.objects.all()
        serializer = Instagram_PostSerializer(instagram_posts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Instagram_PostSerializer)
    def post(self, request):
        serializer = Instagram_PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
    
class Instagram_PostDetailView(APIView):
    @swagger_auto_schema(responses={200: Instagram_PostSerializer})
    def get(self, request, pk):
        try:
            instagram_post = Instagram_Post.objects.get(pk=pk)
            serializer = Instagram_PostSerializer(instagram_post)
            return Response(serializer.data)
        except Instagram_Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Instagram_PostSerializer)
    def put(self, request, pk):
        try:
            instagram_post = Instagram_Post.objects.get(pk=pk)
            serializer = Instagram_PostSerializer(instagram_post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Instagram_Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            instagram_post = Instagram_Post.objects.get(pk=pk)
            instagram_post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Instagram_Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class ZulipListCreateView(APIView):
    @swagger_auto_schema(responses={200: ZulipSerializer(many=True)})
    def get(self, request):
        zulip = Zulip.objects.all()
        serializer = ZulipSerializer(zulip, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ZulipSerializer)
    def post(self, request):
        serializer = ZulipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ZulipDetailView(APIView):
    @swagger_auto_schema(responses={200: ZulipSerializer})
    def get(self, request, pk):
        try:
            zulip = Zulip.objects.get(pk=pk)
            serializer = ZulipSerializer(zulip)
            return Response(serializer.data)
        except Zulip.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=ZulipSerializer)
    def put(self, request, pk):
        try:
            zulip = Zulip.objects.get(pk=pk)
            serializer = ZulipSerializer(zulip, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Zulip.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            zulip = Zulip.objects.get(pk=pk)
            zulip.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Zulip.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Email_BoxListCreateView(APIView):
    @swagger_auto_schema(responses={200: Email_BoxSerializer(many=True)})
    def get(self, request):
        email_boxes = Email_Box.objects.all()
        serializer = Email_BoxSerializer(email_boxes, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Email_BoxSerializer)
    def post(self, request):
        serializer = Email_BoxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Email_BoxDetailView(APIView):
    @swagger_auto_schema(responses={200: Email_BoxSerializer})
    def get(self, request, pk):
        try:
            email_box = Email_Box.objects.get(pk=pk)
            serializer = Email_BoxSerializer(email_box)
            return Response(serializer.data)
        except Email_Box.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Email_BoxSerializer)
    def put(self, request, pk):
        try:
            email_box = Email_Box.objects.get(pk=pk)
            serializer = Email_BoxSerializer(email_box, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Email_Box.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            email_box = Email_Box.objects.get(pk=pk)
            email_box.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Email_Box.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class youtubeListCreateView(APIView):
    @swagger_auto_schema(responses={200: YoutubeSerializer(many=True)})
    def get(self, request):
        youtube = Youtube.objects.all()
        serializer = YoutubeSerializer(youtube, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=YoutubeSerializer)
    def post(self, request):
        serializer = YoutubeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class YoutubeDetailView(APIView):
    @swagger_auto_schema(responses={200: YoutubeSerializer})
    def get(self, request, pk):
        try:
            youtube = Youtube.objects.get(pk=pk)
            serializer = YoutubeSerializer(youtube)
            return Response(serializer.data)
        except Youtube.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=YoutubeSerializer)
    def put(self, request, pk):
        try:
            youtube = Youtube.objects.get(pk=pk)
            serializer = YoutubeSerializer(youtube, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Youtube.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            youtube = Youtube.objects.get(pk=pk)
            youtube.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Youtube.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class BlogListCreateView(APIView):
    @swagger_auto_schema(responses={200: BlogSerializer(many=True)})
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BlogSerializer)
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class BlogDetailView(APIView):
    @swagger_auto_schema(responses={200: BlogSerializer})
    def get(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=BlogSerializer)
    def put(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            serializer = BlogSerializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class VcardListCreateView(APIView):
    @swagger_auto_schema(responses={200: VcardSerializer(many=True)})
    def get(self, request):
        vcards = Vcard.objects.all()
        serializer = VcardSerializer(vcards, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VcardSerializer)
    def post(self, request):
        serializer = VcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class VcardDetailView(APIView):
    @swagger_auto_schema(responses={200: VcardSerializer})
    def get(self, request, pk):
        try:
            vcard = Vcard.objects.get(pk=pk)
            serializer = VcardSerializer(vcard)
            return Response(serializer.data)
        except Vcard.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=VcardSerializer)
    def put(self, request, pk):
        try:
            vcard = Vcard.objects.get(pk=pk)
            serializer = VcardSerializer(vcard, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vcard.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            vcard = Vcard.objects.get(pk=pk)
            vcard.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vcard.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class LMSListCreateView(APIView):
    @swagger_auto_schema(responses={200: LMSSerializer(many=True)})
    def get(self, request):
        lms = LMS.objects.all()
        serializer = LMSSerializer(lms, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LMSSerializer)
    def post(self, request):
        serializer = LMSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LMSDetailView(APIView):
    @swagger_auto_schema(responses={200: LMSSerializer})
    def get(self, request, pk):
        try:
            lms = LMS.objects.get(pk=pk)
            serializer = LMSSerializer(lms)
            return Response(serializer.data)
        except LMS.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=LMSSerializer)
    def put(self, request, pk):
        try:
            lms = LMS.objects.get(pk=pk)
            serializer = LMSSerializer(lms, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except LMS.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            lms = LMS.objects.get(pk=pk)
            lms.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except LMS.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Garden_managementListCreateView(APIView):
    @swagger_auto_schema(responses={200: Garden_managementSerializer(many=True)})
    def get(self, request):
        garden_management = Garden_management.objects.all()
        serializer = Garden_managementSerializer(garden_management, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Garden_managementSerializer)
    def post(self, request):
        serializer = Garden_managementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Garden_managementDetailView(APIView):
    @swagger_auto_schema(responses={200: Garden_managementSerializer})
    def get(self, request, pk):
        try:
            garden_management = Garden_management.objects.get(pk=pk)
            serializer = Garden_managementSerializer(garden_management)
            return Response(serializer.data)
        except Garden_management.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Garden_managementSerializer)
    def put(self, request, pk):
        try:
            garden_management = Garden_management.objects.get(pk=pk)
            serializer = Garden_managementSerializer(garden_management, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Garden_management.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            garden_management = Garden_management.objects.get(pk=pk)
            garden_management.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Garden_management.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Rotas(APIView):
    @swagger_auto_schema(responses={200: RotasSerializer(many=True)})
    def get(self, request):
        rotass = Rotas.objects.all()
        serializer = RotasSerializer(rotass, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RotasSerializer)
    def post(self, request):
        serializer = RotasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RotasDetailView(APIView):
    @swagger_auto_schema(responses={200: RotasSerializer})
    def get(self, request, pk):
        try:
            rotas = Rotas.objects.get(pk=pk)
            serializer = RotasSerializer(rotas)
            return Response(serializer.data)
        except Rotas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=RotasSerializer)
    def put(self, request, pk):
        try:
            rotas = Rotas.objects.get(pk=pk)
            serializer = RotasSerializer(rotas, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Rotas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            rotas = Rotas.objects.get(pk=pk)
            rotas.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Rotas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Comission(APIView):
    @swagger_auto_schema(responses={200: CommisionSerializer(many=True)})
    def get(self, request):
        commissions = Commision.objects.all()
        serializer = CommisionSerializer(commissions, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CommisionSerializer)
    def post(self, request):
        serializer = CommisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ComissionDetailView(APIView):

    @swagger_auto_schema(responses={200: CommisionSerializer})
    def get(self, request, pk):
        try:
            commission = Commision.objects.get(pk=pk)
            serializer = CommisionSerializer(commission)
            return Response(serializer.data)
        except Commision.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=CommisionSerializer)
    def put(self, request, pk):
        try:
            commission = Commision.objects.get(pk=pk)
            serializer = CommisionSerializer(commission, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Commision.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            commission = Commision.objects.get(pk=pk)
            commission.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Commision.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class Agriculture(APIView):
    @swagger_auto_schema(responses={200: AgricultureSerializer(many=True)})
    def get(self, request):
        agriculture = Agriculture.objects.all()
        serializer = AgricultureSerializer(agriculture, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AgricultureSerializer)
    def post(self, request):
        serializer = AgricultureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AgricultureDetailView(APIView):
    @swagger_auto_schema(responses={200: AgricultureSerializer})
    def get(self, request, pk):
        try:
            agriculture = Agriculture.objects.get(pk=pk)
            serializer = AgricultureSerializer(agriculture)
            return Response(serializer.data)
        except Agriculture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=AgricultureSerializer)
    def put(self, request, pk):
        try:
            agriculture = Agriculture.objects.get(pk=pk)
            serializer = AgricultureSerializer(agriculture, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Agriculture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            agriculture = Agriculture.objects.get(pk=pk)
            agriculture.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Agriculture.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class Legal_Case(APIView):
    @swagger_auto_schema(responses={200: Legal_CaseSerializer(many=True)})
    def get(self, request):
        legal_cases = Legal_Case.objects.all()
        serializer = Legal_CaseSerializer(legal_cases, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Legal_CaseSerializer)
    def post(self, request):
        serializer = Legal_CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Legal_CaseDetailView(APIView):    
    @swagger_auto_schema(responses={200: Legal_CaseSerializer})
    def get(self, request, pk):
        try:
            legal_case = Legal_Case.objects.get(pk=pk)
            serializer = Legal_CaseSerializer(legal_case)
            return Response(serializer.data)
        except Legal_Case.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Legal_CaseSerializer)
    def put(self, request, pk):
        try:
            legal_case = Legal_Case.objects.get(pk=pk)
            serializer = Legal_CaseSerializer(legal_case, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Legal_Case.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            legal_case = Legal_Case.objects.get(pk=pk)
            legal_case.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Legal_Case.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class Tour_and_Travel(APIView):
    @swagger_auto_schema(responses={200: Tour_and_TravelSerializer(many=True)})
    def get(self, request):
        tour_and_travel = Tour_and_Travel.objects.all()
        serializer = Tour_and_TravelSerializer(tour_and_travel, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Tour_and_TravelSerializer)
    def post(self, request):
        serializer = Tour_and_TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Tour_and_TravelDetailView(APIView):
    @swagger_auto_schema(responses={200: Tour_and_TravelSerializer})
    def get(self, request, pk):
        try:
            tour_and_travel = Tour_and_Travel.objects.get(pk=pk)
            serializer = Tour_and_TravelSerializer(tour_and_travel)
            return Response(serializer.data)
        except Tour_and_Travel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Tour_and_TravelSerializer)
    def put(self, request, pk):
        try:
            tour_and_travel = Tour_and_Travel.objects.get(pk=pk)
            serializer = Tour_and_TravelSerializer(tour_and_travel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tour_and_Travel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            tour_and_travel = Tour_and_Travel.objects.get(pk=pk)
            tour_and_travel.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tour_and_Travel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Woo_Commerce(APIView):
    @swagger_auto_schema(responses={200: Woo_CommerceSerializer(many=True)})
    def get(self, request):
        woocommerce = Woo_Commerce.objects.all()
        serializer = Woo_CommerceSerializer(woocommerce, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Woo_CommerceSerializer)
    def post(self, request):
        serializer = Woo_CommerceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Woo_CommerceDetailView(APIView):
    @swagger_auto_schema(responses={200: Woo_CommerceSerializer})
    def get(self, request, pk):
        try:
            woocommerce = Woo_Commerce.objects.get(pk=pk)
            serializer = Woo_CommerceSerializer(woocommerce)
            return Response(serializer.data)
        except Woo_Commerce.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Woo_CommerceSerializer)
    def put(self, request, pk):
        try:
            woocommerce = Woo_Commerce.objects.get(pk=pk)
            serializer = Woo_CommerceSerializer(woocommerce, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Woo_Commerce.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            woocommerce = Woo_Commerce.objects.get(pk=pk)
            woocommerce.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Woo_Commerce.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Shopify(APIView):
    @swagger_auto_schema(responses={200: ShopifySerializer(many=True)})
    def get(self, request):
        shopify = Shopify.objects.all()
        serializer = ShopifySerializer(shopify, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ShopifySerializer)
    def post(self, request):
        serializer = ShopifySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ShopifyDetailView(APIView):
    @swagger_auto_schema(responses={200: ShopifySerializer})
    def get(self, request, pk):
        try:
            shopify = Shopify.objects.get(pk=pk)
            serializer = ShopifySerializer(shopify)
            return Response(serializer.data)
        except Shopify.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=ShopifySerializer)
    def put(self, request, pk):
        try:
            shopify = Shopify.objects.get(pk=pk)
            serializer = ShopifySerializer(shopify, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Shopify.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            shopify = Shopify.objects.get(pk=pk)
            shopify.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Shopify.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Indiamart(APIView):
    @swagger_auto_schema(responses={200: IndiamartSerializer(many=True)})
    def get(self, request):
        indiamart = Indiamart.objects.all()
        serializer = IndiamartSerializer(indiamart, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=IndiamartSerializer)
    def post(self, request):
        serializer = IndiamartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class IndiamartDetailView(APIView):
    @swagger_auto_schema(responses={200: IndiamartSerializer})
    def get(self, request, pk):
        try:
            indiamart = Indiamart.objects.get(pk=pk)
            serializer = IndiamartSerializer(indiamart)
            return Response(serializer.data)
        except Indiamart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=IndiamartSerializer)
    def put(self, request, pk):
        try:
            indiamart = Indiamart.objects.get(pk=pk)
            serializer = IndiamartSerializer(indiamart, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Indiamart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            indiamart = Indiamart.objects.get(pk=pk)
            indiamart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Indiamart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class Sage(APIView):
    @swagger_auto_schema(responses={200: SageSerializer(many=True)})
    def get(self, request):
        sage = Sage.objects.all()
        serializer = SageSerializer(sage, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SageSerializer)
    def post(self, request):
        serializer = SageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
class SageDetailView(APIView):
    @swagger_auto_schema(responses={200: SageSerializer})
    def get(self, request, pk):
        try:
            sage = Sage.objects.get(pk=pk)
            serializer = SageSerializer(sage)
            return Response(serializer.data)
        except Sage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=SageSerializer)
    def put(self, request, pk):
        try:
            sage = Sage.objects.get(pk=pk)
            serializer = SageSerializer(sage, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Sage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            sage = Sage.objects.get(pk=pk)
            sage.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Sage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Asana(APIView):
    @swagger_auto_schema(responses={200: AsanaSerializer(many=True)})
    def get(self, request):
        asana = Asana.objects.all()
        serializer = AsanaSerializer(asana, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AsanaSerializer)
    def post(self, request):
        serializer = AsanaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AsanaDetailView(APIView):
    @swagger_auto_schema(responses={200: AsanaSerializer})
    def get(self, request, pk):
        try:
            asana = Asana.objects.get(pk=pk)
            serializer = AsanaSerializer(asana)
            return Response(serializer.data)
        except Asana.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=AsanaSerializer)
    def put(self, request, pk):
        try:
            asana = Asana.objects.get(pk=pk)
            serializer = AsanaSerializer(asana, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Asana.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            asana = Asana.objects.get(pk=pk)
            asana.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Asana.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class Inventory(APIView):
    @swagger_auto_schema(responses={200: InventorySerializer(many=True)})
    def get(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=InventorySerializer)
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
class InventoryDetailView(APIView):
    @swagger_auto_schema(responses={200: InventorySerializer})
    def get(self, request, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(inventory)
            return Response(serializer.data)
        except Inventory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=InventorySerializer)
    def put(self, request, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(inventory, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Inventory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
            inventory.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Inventory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Request(APIView):
    @swagger_auto_schema(responses={200: RequestSerializer(many=True)})
    def get(self, request):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RequestSerializer)
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RequestDetailView(APIView):
    @swagger_auto_schema(responses={200: RequestSerializer})
    def get(self, request, pk):
        try:
            request = Request.objects.get(pk=pk)
            serializer = RequestSerializer(request)
            return Response(serializer.data)
        except Request.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=RequestSerializer)
    def put(self, request, pk):
        try:
            request = Request.objects.get(pk=pk)
            serializer = RequestSerializer(request, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Request.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            request = Request.objects.get(pk=pk)
            request.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Request.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Inovation_Center(APIView):
    @swagger_auto_schema(responses={200: Inovation_CenterSerializer(many=True)})
    def get(self, request):
        inovation_center = Inovation_Center.objects.all()
        serializer = Inovation_CenterSerializer(inovation_center, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Inovation_CenterSerializer)
    def post(self, request):
        serializer = Inovation_CenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Inovation_CenterDetailView(APIView):  
    @swagger_auto_schema(responses={200: Inovation_CenterSerializer})
    def get(self, request, pk):
        try:
            inovation_center = Inovation_Center.objects.get(pk=pk)
            serializer = Inovation_CenterSerializer(inovation_center)
            return Response(serializer.data)
        except Inovation_Center.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Inovation_CenterSerializer)
    def put(self, request, pk):
        try:
            inovation_center = Inovation_Center.objects.get(pk=pk)
            serializer = Inovation_CenterSerializer(inovation_center, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Inovation_Center.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            inovation_center = Inovation_Center.objects.get(pk=pk)
            inovation_center.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Inovation_Center.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Business_Mapping(APIView):
    @swagger_auto_schema(responses={200: Business_MappingSerializer(many=True)})
    def get(self, request):
        business_mapping = Business_Mapping.objects.all()
        serializer = Business_MappingSerializer(business_mapping, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Business_MappingSerializer)
    def post(self, request):
        serializer = Business_MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Business_MappingDetailView(APIView):
    @swagger_auto_schema(responses={200: Business_MappingSerializer})
    def get(self, request, pk):
        try:
            business_mapping = Business_Mapping.objects.get(pk=pk)
            serializer = Business_MappingSerializer(business_mapping)
            return Response(serializer.data)
        except Business_Mapping.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Business_MappingSerializer)
    def put(self, request, pk):
        try:
            business_mapping = Business_Mapping.objects.get(pk=pk)
            serializer = Business_MappingSerializer(business_mapping, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Business_Mapping.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            business_mapping = Business_Mapping.objects.get(pk=pk)
            business_mapping.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Business_Mapping.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class RoadMap_Central(APIView):
    @swagger_auto_schema(responses={200: RoadMap_CentralSerializer(many=True)})
    def get(self, request):
        roadmap_central = RoadMap_Central.objects.all()
        serializer = RoadMap_CentralSerializer(roadmap_central, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RoadMap_CentralSerializer)
    def post(self, request):
        serializer = RoadMap_CentralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RoadMap_CentralDetailView(APIView):
    @swagger_auto_schema(responses={200: RoadMap_CentralSerializer})
    def get(self, request, pk):
        try:
            roadmap_central = RoadMap_Central.objects.get(pk=pk)
            serializer = RoadMap_CentralSerializer(roadmap_central)
            return Response(serializer.data)
        except RoadMap_Central.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=RoadMap_CentralSerializer)
    def put(self, request, pk):
        try:
            roadmap_central = RoadMap_Central.objects.get(pk=pk)
            serializer = RoadMap_CentralSerializer(roadmap_central, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except RoadMap_Central.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            roadmap_central = RoadMap_Central.objects.get(pk=pk)
            roadmap_central.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RoadMap_Central.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Planning(APIView):
    @swagger_auto_schema(responses={200: PlanningSerializer(many=True)})
    def get(self, request):
        planning = Planning.objects.all()
        serializer = PlanningSerializer(planning, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PlanningSerializer)
    def post(self, request):
        serializer = PlanningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PlanningDetailView(APIView):
    @swagger_auto_schema(responses={200: PlanningSerializer})
    def get(self, request, pk):
        try:
            planning = Planning.objects.get(pk=pk)
            serializer = PlanningSerializer(planning)
            return Response(serializer.data)
        except Planning.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=PlanningSerializer)
    def put(self, request, pk):
        try:
            planning = Planning.objects.get(pk=pk)
            serializer = PlanningSerializer(planning, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Planning.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            planning = Planning.objects.get(pk=pk)
            planning.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Planning.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Internal_Knowledge(APIView):
    @swagger_auto_schema(responses={200: Internal_KnowledgeSerializer(many=True)})
    def get(self, request):
        internal_knowledge = Internal_Knowledge.objects.all()
        serializer = Internal_KnowledgeSerializer(internal_knowledge, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Internal_KnowledgeSerializer)
    def post(self, request):
        serializer = Internal_KnowledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Internal_KnowledgeDetailView(APIView):
    @swagger_auto_schema(responses={200: Internal_KnowledgeSerializer})
    def get(self, request, pk):
        try:
            internal_knowledge = Internal_Knowledge.objects.get(pk=pk)
            serializer = Internal_KnowledgeSerializer(internal_knowledge)
            return Response(serializer.data)
        except Internal_Knowledge.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Internal_KnowledgeSerializer)
    def put(self, request, pk):
        try:
            internal_knowledge = Internal_Knowledge.objects.get(pk=pk)
            serializer = Internal_KnowledgeSerializer(internal_knowledge, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Internal_Knowledge.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            internal_knowledge = Internal_Knowledge.objects.get(pk=pk)
            internal_knowledge.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Internal_Knowledge.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Call_Hub(APIView):
    @swagger_auto_schema(responses={200: Call_HubSerializer(many=True)})
    def get(self, request):
        call_hub = Call_Hub.objects.all()
        serializer = Call_HubSerializer(call_hub, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Call_HubSerializer)
    def post(self, request):
        serializer = Call_HubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Call_HubDetailView(APIView):
    @swagger_auto_schema(responses={200: Call_HubSerializer})
    def get(self, request, pk):
        try:
            call_hub = Call_Hub.objects.get(pk=pk)
            serializer = Call_HubSerializer(call_hub)
            return Response(serializer.data)
        except Call_Hub.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Call_HubSerializer)
    def put(self, request, pk):
        try:
            call_hub = Call_Hub.objects.get(pk=pk)
            serializer = Call_HubSerializer(call_hub, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Call_Hub.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            call_hub = Call_Hub.objects.get(pk=pk)
            call_hub.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Call_Hub.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Sendinblue(APIView):
    @swagger_auto_schema(responses={200: SendinblueSerializer(many=True)})
    def get(self, request):
        sendinblue = Sendinblue.objects.all()
        serializer = SendinblueSerializer(sendinblue, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SendinblueSerializer)
    def post(self, request):
        serializer = SendinblueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SendinblueDetailView(APIView):    
    @swagger_auto_schema(responses={200: SendinblueSerializer})
    def get(self, request, pk):
        try:
            sendinblue = Sendinblue.objects.get(pk=pk)
            serializer = SendinblueSerializer(sendinblue)
            return Response(serializer.data)
        except Sendinblue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(request_body=SendinblueSerializer)
    def put(self, request, pk):
        try:
            sendinblue = Sendinblue.objects.get(pk=pk)
            serializer = SendinblueSerializer(sendinblue, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Sendinblue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            sendinblue = Sendinblue.objects.get(pk=pk)
            sendinblue.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Sendinblue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class Side_Menu_Builder(APIView):
    @swagger_auto_schema(responses={200: Side_Menu_BuilderSerializer(many=True)})
    def get(self, request):
        side_menu_builder = Side_Menu_Builder.objects.all()
        serializer = Side_Menu_BuilderSerializer(side_menu_builder, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Side_Menu_BuilderSerializer)
    def post(self, request):
        serializer = Side_Menu_BuilderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Side_Menu_BuilderDetailView(APIView):
    @swagger_auto_schema(responses={200: Side_Menu_BuilderSerializer})
    def get(self, request, pk):
        try:
            side_menu_builder = Side_Menu_Builder.objects.get(pk=pk)
            serializer = Side_Menu_BuilderSerializer(side_menu_builder)
            return Response(serializer.data)
        except Side_Menu_Builder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Side_Menu_BuilderSerializer)
    def put(self, request, pk):
        try:
            side_menu_builder = Side_Menu_Builder.objects.get(pk=pk)
            serializer = Side_Menu_BuilderSerializer(side_menu_builder, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Side_Menu_Builder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            side_menu_builder = Side_Menu_Builder.objects.get(pk=pk)
            side_menu_builder.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Side_Menu_Builder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Activity_Log(APIView):
    @swagger_auto_schema(responses={200: Activity_LogSerializer(many=True)})
    def get(self, request):
        activity_log = Activity_Log.objects.all()
        serializer = Activity_LogSerializer(activity_log, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Activity_LogSerializer)
    def post(self, request):
        serializer = Activity_LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Activity_LogDetailView(APIView):
    @swagger_auto_schema(responses={200: Activity_LogSerializer})
    def get(self, request, pk):
        try:
            activity_log = Activity_Log.objects.get(pk=pk)
            serializer = Activity_LogSerializer(activity_log)
            return Response(serializer.data)
        except Activity_Log.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Activity_LogSerializer)
    def put(self, request, pk):
        try:
            activity_log = Activity_Log.objects.get(pk=pk)
            serializer = Activity_LogSerializer(activity_log, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Activity_Log.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            activity_log = Activity_Log.objects.get(pk=pk)
            activity_log.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Activity_Log.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class OneNote(APIView):
    @swagger_auto_schema(responses={200: OneNoteSerializer(many=True)})
    def get(self, request):
        onenote = OneNote.objects.all()
        serializer = OneNoteSerializer(onenote, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=OneNoteSerializer)
    def post(self, request):
        serializer = OneNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class OneNoteDetailView(APIView):
    @swagger_auto_schema(responses={200: OneNoteSerializer})
    def get(self, request, pk):
        try:
            onenote = OneNote.objects.get(pk=pk)
            serializer = OneNoteSerializer(onenote)
            return Response(serializer.data)
        except OneNote.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=OneNoteSerializer)
    def put(self, request, pk):
        try:
            onenote = OneNote.objects.get(pk=pk)
            serializer = OneNoteSerializer(onenote, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except OneNote.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            onenote = OneNote.objects.get(pk=pk)
            onenote.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except OneNote.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Notes(APIView):
    @swagger_auto_schema(responses={200: NotesSerializer(many=True)})
    def get(self, request):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=NotesSerializer)
    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class NotesDetailView(APIView):
    @swagger_auto_schema(responses={200: NotesSerializer})
    def get(self, request, pk):
        try:
            notes = Notes.objects.get(pk=pk)
            serializer = NotesSerializer(notes)
            return Response(serializer.data)
        except Notes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=NotesSerializer)
    def put(self, request, pk):
        try:
            notes = Notes.objects.get(pk=pk)
            serializer = NotesSerializer(notes, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Notes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            notes = Notes.objects.get(pk=pk)
            notes.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Notes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class Team_Workload(APIView):
    @swagger_auto_schema(responses={200: Team_WorkloadSerializer(many=True)})
    def get(self, request):
        team_workload = Team_Workload.objects.all()
        serializer = Team_WorkloadSerializer(team_workload, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Team_WorkloadSerializer)
    def post(self, request):
        serializer = Team_WorkloadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Team_WorkloadDetailView(APIView):
    @swagger_auto_schema(responses={200: Team_WorkloadSerializer})
    def get(self, request, pk):
        try:
            team_workload = Team_Workload.objects.get(pk=pk)
            serializer = Team_WorkloadSerializer(team_workload)
            return Response(serializer.data)
        except Team_Workload.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Team_WorkloadSerializer)
    def put(self, request, pk):
        try:
            team_workload = Team_Workload.objects.get(pk=pk)
            serializer = Team_WorkloadSerializer(team_workload, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Team_Workload.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            team_workload = Team_Workload.objects.get(pk=pk)
            team_workload.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Team_Workload.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Quiz_Management(APIView):
    @swagger_auto_schema(responses={200: Quiz_ManagementSerializer(many=True)})
    def get(self, request):
        quiz_management = Quiz_Management.objects.all()
        serializer = Quiz_ManagementSerializer(quiz_management, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Quiz_ManagementSerializer)
    def post(self, request):
        serializer = Quiz_ManagementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Quiz_ManagementDetailView(APIView):
    @swagger_auto_schema(responses={200: Quiz_ManagementSerializer})
    def get(self, request, pk):
        try:
            quiz_management = Quiz_Management.objects.get(pk=pk)
            serializer = Quiz_ManagementSerializer(quiz_management)
            return Response(serializer.data)
        except Quiz_Management.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Quiz_ManagementSerializer)
    def put(self, request, pk):
        try:
            quiz_management = Quiz_Management.objects.get(pk=pk)
            serializer = Quiz_ManagementSerializer(quiz_management, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Quiz_Management.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            quiz_management = Quiz_Management.objects.get(pk=pk)
            quiz_management.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Quiz_Management.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Petty_Cash(APIView):
    @swagger_auto_schema(responses={200: Petty_CashSerializer(many=True)})
    def get(self, request):
        petty_cash = Petty_Cash.objects.all()
        serializer = Petty_CashSerializer(petty_cash, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Petty_CashSerializer)
    def post(self, request):
        serializer = Petty_CashSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Petty_CashDetailView(APIView):

    @swagger_auto_schema(responses={200: Petty_CashSerializer})
    def get(self, request, pk):
        try:
            petty_cash = Petty_Cash.objects.get(pk=pk)
            serializer = Petty_CashSerializer(petty_cash)
            return Response(serializer.data)
        except Petty_Cash.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Petty_CashSerializer)
    def put(self, request, pk):
        try:
            petty_cash = Petty_Cash.objects.get(pk=pk)
            serializer = Petty_CashSerializer(petty_cash, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Petty_Cash.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            petty_cash = Petty_Cash.objects.get(pk=pk)
            petty_cash.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Petty_Cash.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class Trello(APIView):
    @swagger_auto_schema(responses={200: TrelloSerializer(many=True)})
    def get(self, request):
        trello = Trello.objects.all()
        serializer = TrelloSerializer(trello, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TrelloSerializer)
    def post(self, request):
        serializer = TrelloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TrelloDetailView(APIView):
    @swagger_auto_schema(responses={200: TrelloSerializer})
    def get(self, request, pk):
        try:
            trello = Trello.objects.get(pk=pk)
            serializer = TrelloSerializer(trello)
            return Response(serializer.data)
        except Trello.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=TrelloSerializer)
    def put(self, request, pk):
        try:
            trello = Trello.objects.get(pk=pk)
            serializer = TrelloSerializer(trello, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Trello.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'}) 
    def delete(self, request, pk):
        try:
            trello = Trello.objects.get(pk=pk)
            trello.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Trello.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class To_Do(APIView):
    @swagger_auto_schema(responses={200: To_DoSerializer(many=True)})
    def get(self, request):
        to_do = To_Do.objects.all()
        serializer = To_DoSerializer(to_do, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=To_DoSerializer)
    def post(self, request):
        serializer = To_DoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class To_DoDetailView(APIView): 
    @swagger_auto_schema(responses={200: To_DoSerializer})
    def get(self, request, pk):
        try:
            to_do = To_Do.objects.get(pk=pk)
            serializer = To_DoSerializer(to_do)
            return Response(serializer.data)
        except To_Do.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=To_DoSerializer)
    def put(self, request, pk):
        try:
            to_do = To_Do.objects.get(pk=pk)
            serializer = To_DoSerializer(to_do, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except To_Do.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            to_do = To_Do.objects.get(pk=pk)
            to_do.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except To_Do.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Time_Tracker(APIView):
    @swagger_auto_schema(responses={200: Time_TrackerSerializer(many=True)})
    def get(self, request):
        time_tracker = Time_Tracker.objects.all()
        serializer = Time_TrackerSerializer(time_tracker, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Time_TrackerSerializer)
    def post(self, request):
        serializer = Time_TrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Time_TrackerDetailView(APIView):
    @swagger_auto_schema(responses={200: Time_TrackerSerializer})
    def get(self, request, pk):
        try:
            time_tracker = Time_Tracker.objects.get(pk=pk)
            serializer = Time_TrackerSerializer(time_tracker)
            return Response(serializer.data)
        except Time_Tracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Time_TrackerSerializer)
    def put(self, request, pk):
        try:
            time_tracker = Time_Tracker.objects.get(pk=pk)
            serializer = Time_TrackerSerializer(time_tracker, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Time_Tracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            time_tracker = Time_Tracker.objects.get(pk=pk)
            time_tracker.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Time_Tracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Timesheet(APIView):
    @swagger_auto_schema(responses={200: TimesheetSerializer(many=True)})
    def get(self, request):
        timesheet = Timesheet.objects.all()
        serializer = TimesheetSerializer(timesheet, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TimesheetSerializer)
    def post(self, request):
        serializer = TimesheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TimesheetDetailView(APIView):
    @swagger_auto_schema(responses={200: TimesheetSerializer})
    def get(self, request, pk):
        try:
            timesheet = Timesheet.objects.get(pk=pk)
            serializer = TimesheetSerializer(timesheet)
            return Response(serializer.data)
        except Timesheet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(request_body=TimesheetSerializer)
    def put(self, request, pk):
        try:
            timesheet = Timesheet.objects.get(pk=pk)
            serializer = TimesheetSerializer(timesheet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Timesheet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            timesheet = Timesheet.objects.get(pk=pk)
            timesheet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Timesheet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Messenger(APIView):
    @swagger_auto_schema(responses={200: MessengerSerializer(many=True)})
    def get(self, request):
        messenger = Messenger.objects.all()
        serializer = MessengerSerializer(messenger, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MessengerSerializer)
    def post(self, request):
        serializer = MessengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MessengerDetailView(APIView):
    @swagger_auto_schema(responses={200: MessengerSerializer})
    def get(self, request, pk):
        try:
            messenger = Messenger.objects.get(pk=pk)
            serializer = MessengerSerializer(messenger)
            return Response(serializer.data)
        except Messenger.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=MessengerSerializer)
    def put(self, request, pk):
        try:
            messenger = Messenger.objects.get(pk=pk)
            serializer = MessengerSerializer(messenger, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Messenger.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            messenger = Messenger.objects.get(pk=pk)
            messenger.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Messenger.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Visitors(APIView):
    @swagger_auto_schema(responses={200: VisitorsSerializer(many=True)})
    def get(self, request):
        visitor = Visitors.objects.all()
        serializer = VisitorsSerializer(visitor, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VisitorsSerializer)
    def post(self, request):
        serializer = VisitorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class VisitorsDetailView(APIView):
    @swagger_auto_schema(responses={200: VisitorsSerializer})
    def get(self, request, pk):
        try:
            visitor = Visitors.objects.get(pk=pk)
            serializer = VisitorsSerializer(visitor)
            return Response(serializer.data)
        except Visitors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=VisitorsSerializer)
    def put(self, request, pk):
        try:
            visitor = Visitors.objects.get(pk=pk)
            serializer = VisitorsSerializer(visitor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Visitors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            visitor = Visitors.objects.get(pk=pk)
            visitor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Visitors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Api_Docs(APIView):
    @swagger_auto_schema(responses={200: Api_DocsSerializer(many=True)})
    def get(self, request):
        api_docs = Api_Docs.objects.all()
        serializer = Api_DocsSerializer(api_docs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Api_DocsSerializer)
    def post(self, request):
        serializer = Api_DocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Api_DocsDetailView(APIView):
    @swagger_auto_schema(responses={200: Api_DocsSerializer})
    def get(self, request, pk):
        try:
            api_docs = Api_Docs.objects.get(pk=pk)
            serializer = Api_DocsSerializer(api_docs)
            return Response(serializer.data)
        except Api_Docs.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Api_DocsSerializer)
    def put(self, request, pk):
        try:
            api_docs = Api_Docs.objects.get(pk=pk)
            serializer = Api_DocsSerializer(api_docs, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Api_Docs.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            api_docs = Api_Docs.objects.get(pk=pk)
            api_docs.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Api_Docs.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Helpdesk(APIView):
    @swagger_auto_schema(responses={200: HelpdeskSerializer(many=True)})
    def get(self, request):
        helpdesk = Helpdesk.objects.all()
        serializer = HelpdeskSerializer(helpdesk, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=HelpdeskSerializer)
    def post(self, request):
        serializer = HelpdeskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HelpdeskDetailView(APIView):
    @swagger_auto_schema(responses={200: HelpdeskSerializer})
    def get(self, request, pk):
        try:
            helpdesk = Helpdesk.objects.get(pk=pk)
            serializer = HelpdeskSerializer(helpdesk)
            return Response(serializer.data)
        except Helpdesk.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=HelpdeskSerializer)
    def put(self, request, pk):
        try:
            helpdesk = Helpdesk.objects.get(pk=pk)
            serializer = HelpdeskSerializer(helpdesk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Helpdesk.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            helpdesk = Helpdesk.objects.get(pk=pk)
            helpdesk.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Helpdesk.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
class Setup_Subscription_plan(APIView):
    @swagger_auto_schema(responses={200: Setup_Subscription_planSerializer(many=True)})
    def get(self, request):
        setup_subscription_plan = Setup_Subscription_plan.objects.all()
        serializer = Setup_Subscription_planSerializer(setup_subscription_plan, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=Setup_Subscription_planSerializer)
    def post(self, request):
        serializer = Setup_Subscription_planSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Setup_Subscription_planDetailView(APIView):
    @swagger_auto_schema(responses={200: Setup_Subscription_planSerializer})
    def get(self, request, pk):
        try:
            setup_subscription_plan = Setup_Subscription_plan.objects.get(pk=pk)
            serializer = Setup_Subscription_planSerializer(setup_subscription_plan)
            return Response(serializer.data)
        except Setup_Subscription_plan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=Setup_Subscription_planSerializer)
    def put(self, request, pk):
        try:
            setup_subscription_plan = Setup_Subscription_plan.objects.get(pk=pk)
            serializer = Setup_Subscription_planSerializer(setup_subscription_plan, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Setup_Subscription_plan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            setup_subscription_plan = Setup_Subscription_plan.objects.get(pk=pk)
            setup_subscription_plan.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Setup_Subscription_plan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class Settings(APIView):
    @swagger_auto_schema(responses={200: SettingsSerializer(many=True)})
    def get(self, request):
        settings = Settings.objects.all()
        serializer = SettingsSerializer(settings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SettingsSerializer)
    def post(self, request):
        serializer = SettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SettingsDetailView(APIView):
    @swagger_auto_schema(responses={200: SettingsSerializer})
    def get(self, request, pk):
        try:
            settings = Settings.objects.get(pk=pk)
            serializer = SettingsSerializer(settings)
            return Response(serializer.data)
        except Settings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(request_body=SettingsSerializer)
    def put(self, request, pk):
        try:
            settings = Settings.objects.get(pk=pk)
            serializer = SettingsSerializer(settings, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Settings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        try:
            settings = Settings.objects.get(pk=pk)
            settings.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Settings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
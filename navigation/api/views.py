import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from navigation.models import MediaBucket
from .serializers import MediaBucketSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import generics
# from rest_framework.generics import APIView
from rest_framework.generics import GenericAPIView 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from navigation.models import Header
from .serializers import HeaderSerializer
from rest_framework import serializers



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from navigation.models import Menu, SubMenu
from .serializers import MenuSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from navigation.models import ( 
    MediaBucket,Header,Menu,SubMenu,Footer,Sectiontwo,Sectionfour,Sectionone,VideoBucket,Sectionthree,Details,Pricingsubdetails,Emailinput,Social,
    Bookacall,Bookacallsectionone,Bookacallsectiontwo,Facts,
    Page,Servicessectionone,Servicessectiontwo,ServicessectionThree,Faq,Servicessectionsix,Servicessectionseven,Pricingdetails,Ourwork,Ourworksectionone,Ourworksectiontwo,Blogs,Blogsectionone,Blogsectiontwo,Blogsectionthree,Blogsectionfour,Pricingsectionfour,CommonSlidersection2,CommonReview,CommonSlidersection1,
    Whyus,Whyussectionseven,Whyussectionsix,Whyussectionfive,Whyussectionfour,Whyussectionthree,Whyussectionfour,Whyussectionthree,Homepage,Sectionfive,Singlereview,Sectionsix,
    Whyussectiontwo,PricingFaq,Pricingsectionthree,Pricingsectiontwo,Pricingsectionone,Pricing,BlogPost,Tag,Blogauthor,BlogPost,Ourworkproject
)

from .serializers import (
    SubMenuSerializer,FooterSerializer,SectiontwoSerializer,HomepageSerializer,OurworkUserSerializer,ServicesuserSerializer,
    SectionfourSerializer,SectiononeSerializer,VideoBucketSerializer,WhyusUserSerializer,bookcallUserSerializer,SocialSerializer,
    SectionthreeSerializer,DetailsSerializer,HomepageReviewSerializer,BlogUserSerializer,blogsingleSerializer,blogpageauthorSerializer,
    BookacallSerializer,BookacallsectiononeSerializer,BookacallsectiontwoSerializer,PageblogSerializer,BlogTimepassUserSerializer,authordetailsSerializer,
    PageSerializer,ServicessectiononeSerializer,ServicessectiontwoSerializer,PageDashboardSerializer,
    ServicessectionThreeSerializer,FaqSerializer,EmailSerializer,SectionsixSerializer,SectionfiveSerializer,singlereviewSerializer,
HomepageSlidersection2Serializer,HomepageSlidersection1Serializer,HomepageReviewSerializer,
    ServicessectionsixSerializer,ServicessectionsevenSerializer,FactsSerializer,
    OurworkSerializer,OurworksectiononeSerializer,OurworksectiontwoSerializer,
    BlogsSerializer,BlogsectiononeSerializer,BlogsectiontwoSerializer,
    BlogsectionthreeSerializer,BlogsectionfourSerializer,WhyusSerializer,
    WhyussectionsevenSerializer,WhyussectionsixSerializer,HomepageSlidersection2Serializer,HomepageSlidersection1Serializer,
    WhyussectionfiveSerializer,WhyussectionfourSerializer,PricingUserSerializer,
    WhyussectionthreeSerializer,WhyussectiontwoSerializer,HomeSerializer,PricingFaqSerializer,
    PricingsectiononeSerializer,PricingSerializer,PricingsectiontwoSerializer,
    PricingsectionthreeSerializer,PricingsectionfourSerializer,PricingdetailsSerializer,ServicesBlogPostSerializer,OurworkprojectSerializer,
    PricingsubdetailsSerializer,ServicesBlogPostSerializer,TagSerializer,BlogauthorSerializer
)


class ImageUploadView(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = MediaBucketSerializer

    def get(self, request):
        images = MediaBucket.objects.all()
        serializer = MediaBucketSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MediaBucketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageUpdateUploadView(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = MediaBucketSerializer

    # def get(self, request):
    #     images = MediaBucket.objects.all()
    #     serializer = MediaBucketSerializer(images, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = MediaBucketSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, image_id):
        try:
            image = MediaBucket.objects.get(id=image_id)
            image_path = image.image.path
            image.delete()
            if os.path.exists(image_path):
                os.remove(image_path)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MediaBucket.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserHeaderView(GenericAPIView):

    serializer_class = HeaderSerializer

    def get(self, request):
        try:
            header = Header.objects.first()  # Retrieve the first and only Header object
            serializer = HeaderSerializer(header)
            return Response(serializer.data)
        except Header.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class HeaderView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = HeaderSerializer

    def get(self, request):
        try:
            header = Header.objects.first()  # Retrieve the first and only Header object
            serializer = HeaderSerializer(header)
            return Response(serializer.data)
        except Header.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            header = Header.objects.first()  # Retrieve the first and only Header object
            serializer = HeaderSerializer(header, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Header.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def post(self, request):
    #     serializer = HeaderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UsernavbarView(GenericAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)


class MenuView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuUpdateView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    def delete(self, request, menu_id):
        try:
            menu = Menu.objects.get(id=menu_id)
            menu.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, menu_id):
        try:
            menu = Menu.objects.get(id=menu_id)
            serializer = MenuSerializer(menu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)




class SubMenuView(GenericAPIView):

    permission_classes = [IsAuthenticated] 
    serializer_class = SubMenuSerializer

    def get(self, request,menu_id):
        try:
            menu = Menu.objects.get(id=menu_id)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
          menus = SubMenu.objects.filter(menu__id=menu_id)
        except SubMenu.DoesNotExist:
            return Response({'error': 'Menu not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubMenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request, menu_id):
        try:
            menu = Menu.objects.get(id=menu_id)
            serializer = SubMenuSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(menu=menu)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SubMenuUpdateView(GenericAPIView):

    permission_classes = [IsAuthenticated] 
    serializer_class = SubMenuSerializer

    def delete(self, request, menu_id, submenu_id):
        try:
            menu = Menu.objects.get(id=menu_id)
            # submenu = menu.submenu_set.get(id=submenu_id)
            submenu = SubMenu.objects.get(menu=menu,id=submenu_id)
            submenu.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except (Menu.DoesNotExist, SubMenu.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, menu_id, submenu_id):
        try:
            menu = Menu.objects.get(id=menu_id)
            # submenu = menu.submenu_set.get(id=submenu_id)
            submenu = SubMenu.objects.get(menu=menu,id=submenu_id)
            serializer = SubMenuSerializer(submenu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (Menu.DoesNotExist, SubMenu.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserFooterView(GenericAPIView):

    serializer_class = FooterSerializer

    def get(self, request):
        try:
            footer = Footer.objects.first()  # Retrieve the first and only Header object
            serializer = FooterSerializer(footer)
            return Response(serializer.data)
        except Footer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FooterView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = FooterSerializer

    def get(self, request):
        try:
            footer = Footer.objects.first()  # Retrieve the first and only Header object
            serializer = FooterSerializer(footer)
            return Response(serializer.data)
        except Footer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            footer = Footer.objects.first()  # Retrieve the first and only Header object
            serializer = FooterSerializer(footer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Footer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class homepageView(GenericAPIView):

    permission_classes = [IsAuthenticated] 
    serializer_class = HomepageSerializer

    def get(self, request):
        try:
            blogs = Homepage.objects.first()
        except Homepage.DoesNotExist:
            blogs = Homepage.objects.create()

        serializer = HomepageSerializer(blogs)
        return Response(serializer.data)

    def put(self, request):
        try:
            blogs = Homepage.objects.first()
        except Homepage.DoesNotExist:
            return Response({'error': 'Homepage page is not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HomepageSerializer(blogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SectiontwoView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = SectiontwoSerializer

    def get(self, request, page_slug):
        try:
            section1 = Sectiontwo.objects.get(page__slug=page_slug)
        except Sectiontwo.DoesNotExist:
            try:
                page = Homepage.objects.get(slug=page_slug)
            except Homepage.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Sectiontwo.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = SectiontwoSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Sectiontwo.objects.get(page__slug=page_slug)
        except Sectiontwo.DoesNotExist:
            return Response({'error': 'Servicessectionone object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectiontwoSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Factsview(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = FactsSerializer

    def get(self, request):
        try:
            # facts = Facts.objects.filter()[:1].filter()  # Get the first object if exists
            facts = Facts.objects.first()
        except Facts.DoesNotExist:
             facts = Facts.objects.create()
            # Perform any additional initialization for the newly created facts object

        serializer = FactsSerializer(facts)
        return Response(serializer.data)

    def put(self, request):
        try:
            ourwork = Facts.objects.first()
        except Facts.DoesNotExist:
            return Response({'error': 'Facts page is not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FactsSerializer(ourwork, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

class UserFactsview(GenericAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = FactsSerializer

    def get(self, request):
        try:
            facts = Facts.objects.filter()[:1].filter()  # Get the first object if exists
        except Facts.DoesNotExist:
             facts = Facts.objects.create()
            # Perform any additional initialization for the newly created facts object

        serializer = FactsSerializer(facts)
        return Response(serializer.data)

class SectionfourView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = SectionfourSerializer

    def get(self, request, page_slug):
        try:
            section1 = Sectionfour.objects.get(page__slug=page_slug)
        except Sectionfour.DoesNotExist:
            try:
                page = Homepage.objects.get(slug=page_slug)
            except Homepage.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Sectionfour.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = SectionfourSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Sectionfour.objects.get(page__slug=page_slug)
        except Sectionfour.DoesNotExist:
            return Response({'error': 'Sectionfour object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectionfourSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SectionfiveView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = SectionfiveSerializer

    def get(self, request, page_slug):
        try:
            section1 = Sectionfive.objects.get(page__slug=page_slug)
        except Sectionfive.DoesNotExist:
            try:
                page = Homepage.objects.get(slug=page_slug)
            except Homepage.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Sectionfive.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = SectionfiveSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Sectionfive.objects.get(page__slug=page_slug)
        except Sectionfive.DoesNotExist:
            return Response({'error': 'Sectionfive object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectionfiveSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class sectionsixView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = SectionsixSerializer

    def get(self, request, page_slug):
        try:
            section1 = Sectionsix.objects.get(page__slug=page_slug)
        except Sectionsix.DoesNotExist:
            try:
                page = Homepage.objects.get(slug=page_slug)
            except Homepage.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Sectionsix.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = SectionsixSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Sectionsix.objects.get(page__slug=page_slug)
        except Sectionsix.DoesNotExist:
            return Response({'error': 'Sectionsix object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectionsixSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class singlereviewView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = singlereviewSerializer

    def get(self, request, page_slug):
        try:
            section1 = Singlereview.objects.get(page__slug=page_slug)
        except Singlereview.DoesNotExist:
            try:
                page = Homepage.objects.get(slug=page_slug)
            except Homepage.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Singlereview.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = singlereviewSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Singlereview.objects.get(page__slug=page_slug)
        except Singlereview.DoesNotExist:
            return Response({'error': 'Singlereview object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = singlereviewSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SectiononeView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = SectiononeSerializer

    def get(self, request, page_slug):
        try:
            section1 = Sectionone.objects.get(page__slug=page_slug)
        except Sectionone.DoesNotExist:
            try:
                page = Homepage.objects.get(slug=page_slug)
            except Homepage.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Sectionone.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = SectiononeSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Sectionone.objects.get(page__slug=page_slug)
        except Sectionone.DoesNotExist:
            return Response({'error': 'Sectionfour object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectiononeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class VideoUploadView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = VideoBucketSerializer

    def get(self, request):
        videos = VideoBucket.objects.all()
        serializer = VideoBucketSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoBucketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoUpdateUploadView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = VideoBucketSerializer

    def delete(self, request, video_id):
        try:
            video = VideoBucket.objects.get(id=video_id)
            video_path = video.video.path
            video.delete()
            if os.path.exists(video_path):
                os.remove(video_path)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except VideoBucket.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SectionthreeView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = SectionthreeSerializer

    def get(self, request, page_slug):
        try:
            section1 = Sectionthree.objects.get(page__slug=page_slug)
        except Sectionthree.DoesNotExist:
            try:
                page = Homepage.objects.get(slug=page_slug)
            except Homepage.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Sectionthree.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = SectionthreeSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Sectionthree.objects.get(page__slug=page_slug)
        except Sectionthree.DoesNotExist:
            return Response({'error': 'Sectionfour object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SectionthreeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DetailsView(GenericAPIView):
    
    # def get(self, request):
    #     details = Details.objects.all()
    #     serializer = DetailsSerializer(details, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = DetailsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, details_id):
    #     try:
    #         details = Details.objects.get(id=details_id)
    #         details.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except Details.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, details_id):
    #     try:
    #         details = Details.objects.get(id=details_id)
    #         serializer = DetailsSerializer(details, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Details.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    permission_classes = [IsAuthenticated]
    serializer_class = DetailsSerializer

    def get_review(self, details_id):
        try:
            review = Details.objects.get(id=details_id)
            return review
        except Details.DoesNotExist:
            return None
    
    def get(self, request, page_slug):
        try:
            page = Homepage.objects.get(slug=page_slug)
        except Homepage.DoesNotExist:
            return Response({'error': 'Homepage not found'}, status=status.HTTP_404_NOT_FOUND)

        reviews = Details.objects.filter(page=page)
        serializer = DetailsSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, page_slug):
        try:
            page = Homepage.objects.get(slug=page_slug)
        except Homepage.DoesNotExist:
            return Response({'error': 'Homepage not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(page=page)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailsUpdateView(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = DetailsSerializer


    def get_review(self, details_id):
        try:
            review = Details.objects.get(id=details_id)
            return review
        except Details.DoesNotExist:
            return None
    
    def get(self, request, page_slug, details_id):
        try:
            page = Homepage.objects.get(slug=page_slug)
        except Homepage.DoesNotExist:
            return Response({'error': 'Homepage not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
          reviews = Details.objects.get(page=page,id=details_id)
        except Details.DoesNotExist:
            return Response({'error': 'details not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DetailsSerializer(reviews)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request,page_slug, details_id):
        try:
            page = Homepage.objects.get(slug=page_slug)
        except Homepage.DoesNotExist:
            return Response({'error': 'Homepage not found'}, status=status.HTTP_404_NOT_FOUND)
        review = self.get_review(details_id)
        if not review:
            return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetailsSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,page_slug, details_id):
        try:
            page = Homepage.objects.get(slug=page_slug)
        except Homepage.DoesNotExist:
            return Response({'error': 'Homepage not found'}, status=status.HTTP_404_NOT_FOUND)
        review = self.get_review(details_id)
        if not review:
            return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserHomepageReviewView(GenericAPIView):
    
    # def get(self, request):
    #     details = HomepageReview.objects.all()
    #     serializer = HomepageReviewSerializer(details, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = HomepageReviewSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, review_id):
    #     try:
    #         details = HomepageReview.objects.get(id=review_id)
    #         details.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except HomepageReview.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, review_id):
    #     try:
    #         details = HomepageReview.objects.get(id=review_id)
    #         serializer = HomepageReviewSerializer(details, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except HomepageReview.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    serializer_class = HomepageReviewSerializer

    def get(self, request):
        menus = CommonReview.objects.all()
        serializer = HomepageReviewSerializer(menus, many=True)
        return Response(serializer.data)


class HomepageReviewView(GenericAPIView):
    
    # def get(self, request):
    #     details = HomepageReview.objects.all()
    #     serializer = HomepageReviewSerializer(details, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = HomepageReviewSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, review_id):
    #     try:
    #         details = HomepageReview.objects.get(id=review_id)
    #         details.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except HomepageReview.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, review_id):
    #     try:
    #         details = HomepageReview.objects.get(id=review_id)
    #         serializer = HomepageReviewSerializer(details, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except HomepageReview.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    permission_classes = [IsAuthenticated]
    serializer_class = HomepageReviewSerializer

    def get(self, request):
        menus = CommonReview.objects.all()
        serializer = HomepageReviewSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HomepageReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomepageUpdateReviewView(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = HomepageReviewSerializer

    def delete(self, request, review_id):
        try:
            menu = CommonReview.objects.get(id=review_id)
            menu.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CommonReview.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, review_id):
        try:
            menu = CommonReview.objects.get(id=review_id)
            serializer = HomepageReviewSerializer(menu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CommonReview.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class HomepageSlidersection1View(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = HomepageSlidersection1Serializer



    def get(self, request):
        menus = CommonSlidersection1.objects.all()
        serializer = HomepageSlidersection1Serializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HomepageSlidersection1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class HomepageSlidersection1updateView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = HomepageSlidersection2Serializer

    # def get_image(self, image_id):
    #     try:
    #         review = HomepageSlidersection1.objects.get(id=image_id)
    #         return review
    #     except HomepageSlidersection1.DoesNotExist:
    #         return None

    # def get(self, request, page_slug, image_id):
    #     try:
    #         page = Homepage.objects.get(slug=page_slug)
    #     except Homepage.DoesNotExist:
    #         return Response({'error': 'Homepage Page not found'}, status=status.HTTP_404_NOT_FOUND)
    #     image = self.get_image(image_id)
    #     if image is None:
    #         return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

    #     # images = HomepageSlidersection1.objects.filter(page=page)
    #     serializer = HomepageSlidersection1Serializer(image)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request , page_slug , image_id):
    #     try:
    #         page = Homepage.objects.get(slug=page_slug)
    #     except Homepage.DoesNotExist:
    #         return Response({'error': 'Homepage Page not found'}, status=status.HTTP_404_NOT_FOUND)
    #     image = self.get_image(image_id)
    #     if image is None:
    #         return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = HomepageSlidersection1Serializer(image, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request , page_slug , image_id):
    #     try:
    #         page = Homepage.objects.get(slug=page_slug)
    #     except Homepage.DoesNotExist:
    #         return Response({'error': 'Homepage Page not found'}, status=status.HTTP_404_NOT_FOUND)
    #     image = self.get_image(image_id)
    #     if image is None:
    #         return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

    #     image.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, image_id):
        try:
            menu = CommonSlidersection2.objects.get(id=image_id)
            menu.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CommonSlidersection2.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, image_id):
        try:
            menu = CommonSlidersection2.objects.get(id=image_id)
            serializer = HomepageSlidersection2Serializer(menu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CommonSlidersection2.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class UserHomepageSlidersection2View(GenericAPIView):

    serializer_class = HomepageSlidersection2Serializer

    def get(self, request):
        menus = CommonSlidersection2.objects.all()
        serializer = HomepageSlidersection2Serializer(menus, many=True)
        return Response(serializer.data)

class UserHomepageSlidersection1View(GenericAPIView):

    serializer_class = HomepageSlidersection1Serializer

    def get(self, request):
        menus = CommonSlidersection1.objects.all()
        serializer = HomepageSlidersection1Serializer(menus, many=True)
        return Response(serializer.data)

class HomepageSlidersection2View(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = HomepageSlidersection2Serializer

    def get(self, request):
        menus = CommonSlidersection1.objects.all()
        serializer = HomepageSlidersection1Serializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HomepageSlidersection1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomepageUpdateSlidersection2View(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = HomepageSlidersection2Serializer

    def delete(self, request, image_id):
        try:
            menu = CommonSlidersection2.objects.get(id=image_id)
            menu.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CommonSlidersection2.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, image_id):
        try:
            menu = CommonSlidersection2.objects.get(id=image_id)
            serializer = HomepageSlidersection2Serializer(menu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CommonSlidersection2.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PagelistView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PageDashboardSerializer

    def get(self, request):
        pages = Page.objects.all()
        serializer = PageDashboardSerializer(pages, many=True)
        return Response(serializer.data)



    def post(self, request):
        serializer = PageDashboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.core.exceptions import ObjectDoesNotExist




class PageView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PageDashboardSerializer

    def get(self, request,page_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found error'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PageDashboardSerializer(page)
        return Response(serializer.data)

    # def get(self, request, page_slug):
    #     try:
    #         page = Page.objects.get(slug=page_slug)
    #     except Page.DoesNotExist:
    #         return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

    #     reviews = Servicesreview.objects.filter(page=page)
    #     serializer = ServicesreviewSerializer(reviews, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)



    def delete(self, request, page_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except ObjectDoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, page_slug):
        try:
            page = Page.objects.get(slug=page_slug)
            serializer = PageDashboardSerializer(page, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Page.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# class ServicessectiononeView(GenericAPIView):
#     def get(self, request, page_slug):
#         try:
#             section1 = Servicessectionone.objects.get(page__slug=page_slug)
#         except Servicessectionone.DoesNotExist:
#             return Response({'error': 'Servicessectionone object not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = ServicessectiononeSerializer(section1)
#         return Response(serializer.data)

#     def put(self, request, page_slug):
#         try:
#             section1 = Servicessectionone.objects.get(page__slug=page_slug)
#         except Servicessectionone.DoesNotExist:
#             return Response({'error': 'Servicessectionone object not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = ServicessectiononeSerializer(section1, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ServicessectiononeView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ServicessectiononeSerializer

    def get(self, request, page_slug):
        try:
            section1 = Servicessectionone.objects.get(page__slug=page_slug)
        except Servicessectionone.DoesNotExist:
            try:
                page = Page.objects.get(slug=page_slug)
            except Page.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Servicessectionone.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = ServicessectiononeSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Servicessectionone.objects.get(page__slug=page_slug)
        except Servicessectionone.DoesNotExist:
            return Response({'error': 'Servicessectionone object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServicessectiononeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ServicessectiontwoView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ServicessectiontwoSerializer

    def get(self, request, page_slug):
        try:
            section1 = Servicessectiontwo.objects.get(page__slug=page_slug)
        except Servicessectiontwo.DoesNotExist:
            try:
                page = Page.objects.get(slug=page_slug)
            except Page.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Servicessectiontwo.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = ServicessectiontwoSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Servicessectiontwo.objects.get(page__slug=page_slug)
        except Servicessectiontwo.DoesNotExist:
            return Response({'error': 'Servicessectiontwo object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServicessectiontwoSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicessectionThreeView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ServicessectionThreeSerializer

    def get(self, request, page_slug):
        try:
            section1 = ServicessectionThree.objects.get(page__slug=page_slug)
        except ServicessectionThree.DoesNotExist:
            try:
                page = Page.objects.get(slug=page_slug)
            except Page.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = ServicessectionThree.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = ServicessectionThreeSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = ServicessectionThree.objects.get(page__slug=page_slug)
        except ServicessectionThree.DoesNotExist:
            return Response({'error': 'ServicessectionThree object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServicessectionThreeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ServicesreviewView(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = ServicesreviewSerializer

#     def get_review(self, review_id):
#         try:
#             review = Servicesreview.objects.get(id=review_id)
#             return review
#         except Servicesreview.DoesNotExist:
#             return None
    
#     def get(self, request, page_slug):
#         try:
#             page = Page.objects.get(slug=page_slug)
#         except Page.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

#         reviews = Servicesreview.objects.filter(page=page)
#         serializer = ServicesreviewSerializer(reviews, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, page_slug):
#         try:
#             page = Page.objects.get(slug=page_slug)
#         except Page.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = ServicesreviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(page=page)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ServicesreviewUpdateView(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = ServicesreviewSerializer

#     def get_review(self, review_id):
#         try:
#             review = Servicesreview.objects.get(id=review_id)
#             return review
#         except Servicesreview.DoesNotExist:
#             return None
    
#     def get(self, request, page_slug, review_id):
#         try:
#             page = Page.objects.get(slug=page_slug)
#         except Page.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

#         try:
#           reviews = Servicesreview.objects.get(page=page,id=review_id)
#         except Servicesreview.DoesNotExist:
#             return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = ServicesreviewSerializer(reviews)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request,page_slug, review_id):
#         review = self.get_review(review_id)
#         if not review:
#            return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = ServicesreviewSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request,page_slug, review_id):
#         try:
#             page = Page.objects.get(slug=page_slug)
#         except Page.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         review = self.get_review(review_id)
#         if not review:
#             return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class FaqView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = FaqSerializer

    def get_faq(self, faq_id):
        try:
            faq = Faq.objects.get(id=faq_id)
            return faq
        except Servicesreview.DoesNotExist:
            return None
    
    def get(self, request, page_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

        reviews = Faq.objects.filter(page=page)
        serializer = FaqSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, page_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(page=page)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FaqUpdateView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = FaqSerializer

    def get_faq(self, faq_id):
        try:
            faq = Faq.objects.get(id=faq_id)
            return faq
        except Faq.DoesNotExist:
            return None
    
    def get(self, request, page_slug, faq_id):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
          reviews = Faq.objects.get(page=page,id=faq_id)
        except Faq.DoesNotExist:
            return Response({'error': 'Faq not found'}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = FaqSerializer(reviews)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request,page_slug, faq_id):
    
         faq = self.get_faq(faq_id)
         if not faq:
            return Response({'error': 'faq not found'}, status=status.HTTP_404_NOT_FOUND)


         serializer = FaqSerializer(faq, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,page_slug, faq_id):
        try:
         faq = self.get_faq(faq_id)
        except faq.DoesNotExist:
            return Response({'error': 'Faq not found'}, status=status.HTTP_404_NOT_FOUND)
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServicessectionsixView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ServicessectionsixSerializer

    def get(self, request, page_slug):
        try:
            section1 = Servicessectionsix.objects.get(page__slug=page_slug)
        except Servicessectionsix.DoesNotExist:
            try:
                page = Page.objects.get(slug=page_slug)
            except Page.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Servicessectionsix.objects.create(page=page)
            # Perform any additional initialization for the newly created section1 object

        serializer = ServicessectionsixSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Servicessectionsix.objects.get(page__slug=page_slug)
        except Servicessectionsix.DoesNotExist:
            return Response({'error': 'Servicessectionsix object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServicessectionsixSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ServicessectionsevenView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ServicessectionsevenSerializer

    def get(self, request, page_slug):
        try:
            section1 = Servicessectionseven.objects.get(page__slug=page_slug)
        except Servicessectionseven.DoesNotExist:
            try:
                page = Page.objects.get(slug=page_slug)
            except Page.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Servicessectionseven.objects.create(page=page)

        serializer = ServicessectionsevenSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Servicessectionseven.objects.get(page__slug=page_slug)
        except Servicessectionseven.DoesNotExist:
            return Response({'error': 'Servicessectionseven object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServicessectionsevenSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class SlidersectionView(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = SlidersectionSerializer

#     def get_image(self, image_id):
#         try:
#             review = Slidersection.objects.get(id=image_id)
#             return review
#         except Slidersection.DoesNotExist:
#             return None
    
#     def get(self, request, page_slug):
#         try:
#             page = Page.objects.get(slug=page_slug)
#         except Page.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

#         images = Slidersection.objects.filter(page=page)
#         serializer = SlidersectionSerializer(images, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def post(self, request, page_slug):
#         try:
#             page = Page.objects.get(slug=page_slug)
#         except Page.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = SlidersectionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(page=page)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SlidersectionUpdateView(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = SlidersectionSerializer


#     def get_image(self, image_id):
#         try:
#             review = Slidersection.objects.get(id=image_id)
#             return review
#         except Slidersection.DoesNotExist:
#             return None
    
#     def get(self, request, page_slug, image_id):
#         try:
#             page = Page.objects.get(slug=page_slug)
#         except Page.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

#         try:
#           images = Slidersection.objects.get(page=page,id=image_id)
#         except Slidersection.DoesNotExist:
#             return Response({'error': 'image id  not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = SlidersectionSerializer(images)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request,page_slug, image_id):
#         image = self.get_image(image_id)
#         if image is None:
#             return Response({'error': 'image not found'}, status=status.HTTP_404_NOT_FOUND)

#         try:
#             page = Page.objects.get(slug=page_slug)
#         except Page.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = SlidersectionSerializer(image, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request,page_slug, image_id):
#         image = self.get_image(image_id)
#         if image is None:
#             return Response({'error': 'image not found'}, status=status.HTTP_404_NOT_FOUND)

#         try:
#             page = Page.objects.get(slug=page_slug)
#         except Page.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

#         image.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class servicesview(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = HomeSerializer

    def get(self, request):
        try:
            blogs = Homepage.objects.first()
        except Homepage.DoesNotExist:
            return Response({'error': 'please create a homepage template in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HomeSerializer(blogs)
        return Response(serializer.data)

class OurworkView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = OurworkSerializer

    def get(self, request):
        try:
            ourwork = Ourwork.objects.first()
        except Ourwork.DoesNotExist:
            ourwork = Ourwork.objects.create()

        serializer = OurworkSerializer(ourwork)
        return Response(serializer.data)

    def put(self, request):
        try:
            ourwork = Ourwork.objects.first()
        except Ourwork.DoesNotExist:
            return Response({'error': 'ourwork page is not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OurworkSerializer(ourwork, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OurworksectiononeView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = OurworksectiononeSerializer

    def get(self, request, page_slug):
        try:
            section1 = Ourworksectionone.objects.get(page__slug=page_slug)
        except Ourworksectionone.DoesNotExist:
            try:
                page = Ourwork.objects.get(slug=page_slug)
            except Ourwork.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Ourworksectionone.objects.create(page=page)

        serializer = OurworksectiononeSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Ourworksectionone.objects.get(page__slug=page_slug)
        except Ourworksectionone.DoesNotExist:
            return Response({'error': 'Ourworksectionone object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OurworksectiononeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OurworksectiontwoView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = OurworksectiontwoSerializer

    def get(self, request, page_slug):
        try:
            section1 = Ourworksectiontwo.objects.get(page__slug=page_slug)
        except Ourworksectiontwo.DoesNotExist:
            try:
                page = Ourwork.objects.get(slug=page_slug)
            except Ourwork.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Ourworksectiontwo.objects.create(page=page)

        serializer = OurworksectiontwoSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Ourworksectiontwo.objects.get(page__slug=page_slug)
        except Ourworksectiontwo.DoesNotExist:
            return Response({'error': 'Servicessectionseven object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OurworksectiontwoSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class BlogsView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BlogsSerializer

    def get(self, request):
        try:
            blogs = Blogs.objects.first()
        except Blogs.DoesNotExist:
            blogs = Blogs.objects.create()

        serializer = BlogsSerializer(blogs)
        return Response(serializer.data)

    def put(self, request):
        try:
            blogs = Blogs.objects.first()
        except Blogs.DoesNotExist:
            return Response({'error': 'ourwork page is not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogsSerializer(blogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogssectiononeView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BlogsectiononeSerializer

    def get(self, request, page_slug):
        try:
            section1 = Blogsectionone.objects.get(page__slug=page_slug)
        except Blogsectionone.DoesNotExist:
            try:
                page = Blogs.objects.get(slug=page_slug)
            except Blogs.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Blogsectionone.objects.create(page=page)

        serializer = BlogsectiononeSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Blogsectionone.objects.get(page__slug=page_slug)
        except Blogsectionone.DoesNotExist:
            return Response({'error': 'Ourworksectionone object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogsectiononeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogssectiontwoView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BlogsectiontwoSerializer

    def get(self, request, page_slug):
        try:
            section2 = Blogsectiontwo.objects.get(page__slug=page_slug)
        except Blogsectiontwo.DoesNotExist:
            try:
                page = Blogs.objects.get(slug=page_slug)
            except Blogs.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Blogsectiontwo.objects.create(page=page)

        serializer = BlogsectiontwoSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Blogsectiontwo.objects.get(page__slug=page_slug)
        except Blogsectiontwo.DoesNotExist:
            return Response({'error': 'Servicessectionseven object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogsectiontwoSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogssectionthreeView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BlogsectionthreeSerializer

    def get(self, request, page_slug):
        try:
            section2 = Blogsectionthree.objects.get(page__slug=page_slug)
        except Blogsectionthree.DoesNotExist:
            try:
                page = Blogs.objects.get(slug=page_slug)
            except Blogs.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Blogsectionthree.objects.create(page=page)

        serializer = BlogsectionthreeSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Blogsectionthree.objects.get(page__slug=page_slug)
        except Blogsectionthree.DoesNotExist:
            return Response({'error': 'blogsectionthree page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogsectionthreeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogssectionfourView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BlogsectionfourSerializer

    def get(self, request, page_slug):
        try:
            section2 = Blogsectionfour.objects.get(page__slug=page_slug)
        except Blogsectionfour.DoesNotExist:
            try:
                page = Blogs.objects.get(slug=page_slug)
            except Blogs.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Blogsectionfour.objects.create(page=page)

        serializer = BlogsectionfourSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Blogsectionfour.objects.get(page__slug=page_slug)
        except Blogsectionfour.DoesNotExist:
            return Response({'error': 'blogsectionfour page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogsectionfourSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhyusView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = WhyusSerializer

    def get(self, request):
        try:
            blogs = Whyus.objects.first()
        except Whyus.DoesNotExist:
            blogs = Whyus.objects.create()

        serializer = WhyusSerializer(blogs)
        return Response(serializer.data)

    def put(self, request):
        try:
            blogs = Whyus.objects.first()
        except Whyus.DoesNotExist:
            return Response({'error': 'ourwork page is not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WhyusSerializer(blogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhyussectionsevenView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = WhyussectionsevenSerializer


    def get(self, request, page_slug):
        try:
            section2 = Whyussectionseven.objects.get(page__slug=page_slug)
        except Whyussectionseven.DoesNotExist:
            try:
                page = Whyus.objects.get(slug=page_slug)
            except Whyus.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Whyussectionseven.objects.create(page=page)

        serializer = WhyussectionsevenSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Whyussectionseven.objects.get(page__slug=page_slug)
        except Whyussectionseven.DoesNotExist:
            return Response({'error': 'Whyussectionseven page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WhyussectionsevenSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhyussectionsixView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = WhyussectionsixSerializer

    def get(self, request, page_slug):
        try:
            section2 = Whyussectionsix.objects.get(page__slug=page_slug)
        except Whyussectionsix.DoesNotExist:
            try:
                page = Whyus.objects.get(slug=page_slug)
            except Whyus.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Whyussectionsix.objects.create(page=page)

        serializer = WhyussectionsixSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Whyussectionsix.objects.get(page__slug=page_slug)
        except Whyussectionsix.DoesNotExist:
            return Response({'error': 'blogsectionfour page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WhyussectionsixSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhyussectionfiveView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = WhyussectionfiveSerializer

    def get(self, request, page_slug):
        try:
            section2 = Whyussectionfive.objects.get(page__slug=page_slug)
        except Whyussectionfive.DoesNotExist:
            try:
                page = Whyus.objects.get(slug=page_slug)
            except Whyus.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Whyussectionfive.objects.create(page=page)

        serializer = WhyussectionfiveSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Whyussectionfive.objects.get(page__slug=page_slug)
        except Whyussectionfive.DoesNotExist:
            return Response({'error': 'blogsectionfour page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WhyussectionfiveSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhyussectionfourView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = WhyussectionfourSerializer

    def get(self, request, page_slug):
        try:
            section2 = Whyussectionfour.objects.get(page__slug=page_slug)
        except Whyussectionfour.DoesNotExist:
            try:
                page = Whyus.objects.get(slug=page_slug)
            except Whyus.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Whyussectionfour.objects.create(page=page)

        serializer = WhyussectionfourSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Whyussectionfour.objects.get(page__slug=page_slug)
        except Whyussectionfour.DoesNotExist:
            return Response({'error': 'blogsectionfour page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WhyussectionfourSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhyussectionthreeView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = WhyussectionthreeSerializer

    def get(self, request, page_slug):
        try:
            section2 = Whyussectionthree.objects.get(page__slug=page_slug)
        except Whyussectionthree.DoesNotExist:
            try:
                page = Whyus.objects.get(slug=page_slug)
            except Whyus.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Whyussectionthree.objects.create(page=page)

        serializer = WhyussectionthreeSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Whyussectionthree.objects.get(page__slug=page_slug)
        except Whyussectionthree.DoesNotExist:
            return Response({'error': 'blogsectionfour page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WhyussectionthreeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhyussectiontwoView(GenericAPIView): 

    permission_classes = [IsAuthenticated]
    serializer_class = WhyussectiontwoSerializer

    def get(self, request, page_slug):
        try:
            section2 = Whyussectiontwo.objects.get(page__slug=page_slug)
        except Whyussectiontwo.DoesNotExist:
            try:
                page = Whyus.objects.get(slug=page_slug)
            except Whyus.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Whyussectiontwo.objects.create(page=page)

        serializer = WhyussectiontwoSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Whyussectiontwo.objects.get(page__slug=page_slug)
        except Whyussectiontwo.DoesNotExist:
            return Response({'error': 'blogsectionfour page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WhyussectiontwoSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PricingView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PricingSerializer

    def get(self, request):
        try:
            blogs = Pricing.objects.first()
        except Pricing.DoesNotExist:
            blogs = Pricing.objects.create()

        serializer = PricingSerializer(blogs)
        return Response(serializer.data)

    def put(self, request):
        try:
            blogs = Pricing.objects.first()
        except Pricing.DoesNotExist:
            return Response({'error': 'ourwork page is not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PricingSerializer(blogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PricingsectiononeView(GenericAPIView): 

    permission_classes = [IsAuthenticated]
    serializer_class = PricingsectiononeSerializer

    def get(self, request, page_slug):
        try:
            section2 = Pricingsectionone.objects.get(page__slug=page_slug)
        except Pricingsectionone.DoesNotExist:
            try:
                page = Pricing.objects.get(slug=page_slug)
            except Pricing.DoesNotExist:
                return Response({'error': 'Pricing Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Pricingsectionone.objects.create(page=page)

        serializer = PricingsectiononeSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Pricingsectionone.objects.get(page__slug=page_slug)
        except Pricingsectionone.DoesNotExist:
            return Response({'error': 'blogsectionfour page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PricingsectiononeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PricingsectiontwoView(GenericAPIView): 

    permission_classes = [IsAuthenticated]
    serializer_class = PricingsectiontwoSerializer

    def get(self, request, page_slug):
        try:
            section2 = Pricingsectiontwo.objects.get(page__slug=page_slug)
        except Pricingsectiontwo.DoesNotExist:
            try:
                page = Pricing.objects.get(slug=page_slug)
            except Pricing.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Pricingsectiontwo.objects.create(page=page)

        serializer = PricingsectiontwoSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Pricingsectiontwo.objects.get(page__slug=page_slug)
        except Pricingsectiontwo.DoesNotExist:
            return Response({'error': 'Pricingsectiontwo page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PricingsectiontwoSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PricingsectionthreeView(GenericAPIView): 

    permission_classes = [IsAuthenticated]
    serializer_class = PricingsectionthreeSerializer

    def get(self, request, page_slug):
        try:
            section2 = Pricingsectionthree.objects.get(page__slug=page_slug)
        except Pricingsectionthree.DoesNotExist:
            try:
                page = Pricing.objects.get(slug=page_slug)
            except Pricing.DoesNotExist:
                return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Pricingsectionthree.objects.create(page=page)

        serializer = PricingsectionthreeSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Pricingsectionthree.objects.get(page__slug=page_slug)
        except Pricingsectionthree.DoesNotExist:
            return Response({'error': 'Pricingsectionthree page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PricingsectionthreeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @swagger_auto_schema(request_body=PricingsectionfourSerializer, method='post')
class PricingsectionfourView(GenericAPIView): 

    permission_classes = [IsAuthenticated]

    serializer_class = PricingsectionfourSerializer

    def get(self, request, page_slug):
        try:
            section2 = Pricingsectionfour.objects.get(page__slug=page_slug)
        except Pricingsectionfour.DoesNotExist:
            try:
                page = Pricing.objects.get(slug=page_slug)
            except Pricing.DoesNotExist:
                return Response({'error': 'Pricingsectionfour Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section2 = Pricingsectionfour.objects.create(page=page)

        serializer = PricingsectionfourSerializer(section2)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Pricingsectionfour.objects.get(page__slug=page_slug)
        except Pricingsectionfour.DoesNotExist:
            return Response({'error': 'Pricingsectionfour page not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PricingsectionfourSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class PricinguserreviewView(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = PricinguserreviewSerializer

#     def get(self, request,page_slug):
#         try:
#             page = Pricing.objects.get(slug=page_slug)
#         except Pricing.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         details = Pricinguserreview.objects.all()
#         serializer = PricinguserreviewSerializer(details, many=True)
#         return Response(serializer.data)

#     def post(self, request,page_slug):
#         try:
#             page = Pricing.objects.get(slug=page_slug)
#         except Pricing.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = PricinguserreviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(page=page)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PricinguserUpdatereviewView(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = PricinguserreviewSerializer

#     def get(self, request,page_slug,review_id):
#         try:
#             page = Pricing.objects.get(slug=page_slug)
#         except Pricing.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         try:
#            details = Pricinguserreview.objects.get(id=review_id)
#         except Pricinguserreview.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = PricinguserreviewSerializer(details)
#         return Response(serializer.data)

#     def delete(self, request,page_slug, review_id):
#         try:
#             page = Pricing.objects.get(slug=page_slug)
#         except Pricing.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         try:
#             details = Pricinguserreview.objects.get(id=review_id)
#             details.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Pricinguserreview.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self, request,page_slug, review_id):
#         try:
#             page = Pricing.objects.get(slug=page_slug)
#         except Pricing.DoesNotExist:
#             return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         try:
#             details = Pricinguserreview.objects.get(id=review_id)
#             serializer = PricinguserreviewSerializer(details, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Pricinguserreview.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)



class PricingFaqView(GenericAPIView):
    

    permission_classes = [IsAuthenticated]
    serializer_class = PricingFaqSerializer

    def get(self, request,page_slug):

        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        details = PricingFaq.objects.all()
        serializer = PricingFaqSerializer(details, many=True)
        return Response(serializer.data)

    def post(self, request,page_slug):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PricingFaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(page=page)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PricingUpdateFaqView(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = PricingFaqSerializer

    def get(self, request,page_slug, review_id):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
          details = PricingFaq.objects.get(id=review_id)
        except PricingFaq.DoesNotExist:
            return Response({'error': 'review not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PricingFaqSerializer(details)
        return Response(serializer.data)

    def delete(self, request,page_slug, review_id):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            details = PricingFaq.objects.get(id=review_id)
            details.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PricingFaq.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request,page_slug, review_id):
        try:
            details = PricingFaq.objects.get(id=review_id)
            serializer = PricingFaqSerializer(details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PricingFaq.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PricingdetailsView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PricingdetailsSerializer

    def get(self, request,page_slug):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        details = Pricingdetails.objects.all()
        serializer = PricingdetailsSerializer(details, many=True)
        return Response(serializer.data)

    def post(self, request,page_slug):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PricingdetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(page=page)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PricingUpdatedetailsView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PricingdetailsSerializer

    def get(self, request,page_slug,review_id):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
          details = Pricingdetails.objects.get(id=review_id)
        except Pricingdetails.DoesNotExist:
            return Response({'error': 'review not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PricingdetailsSerializer(details)
        return Response(serializer.data)

    def delete(self, request,page_slug, review_id):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            details = Pricingdetails.objects.get(id=review_id)
            details.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pricingdetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request,page_slug, review_id):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            details = Pricingdetails.objects.get(id=review_id)
            serializer = PricingdetailsSerializer(details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pricingdetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PricingsubdetailsView(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = PricingsubdetailsSerializer

    def get(self, request,page_slug,review_id):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
          details = Pricingsubdetails.objects.filter(pricingpage__id=review_id)
        except Pricingsubdetails.DoesNotExist:
            return Response({'error': 'Pricingsubdetails Page not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PricingsubdetailsSerializer(details, many=True)
        return Response(serializer.data)

    def post(self, request,page_slug,review_id):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            page = Pricingdetails.objects.get(id=review_id)
        except Pricingdetails.DoesNotExist:
            return Response({'error': 'Pricingdetails not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PricingsubdetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(pricingpage=page)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PricingUpdatesubdetailsView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PricingsubdetailsSerializer

    def get(self, request,page_slug,review_id,subreview_id):
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
          details = Pricingdetails.objects.get(id=review_id)
        except Pricingdetails.DoesNotExist:
            return Response({'error': 'review id not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
          details = Pricingsubdetails.objects.get(pricingpage__id=review_id,id=subreview_id)
        except Pricingsubdetails.DoesNotExist:
            return Response({'error': 'Pricingsubdetails Page not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PricingsubdetailsSerializer(details)
        return Response(serializer.data)

    def delete(self, request,page_slug, review_id,subreview_id):
        try:
          details = Pricingdetails.objects.get(id=review_id)
        except Pricingdetails.DoesNotExist:
            return Response({'error': 'review id not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            details = Pricingsubdetails.objects.get(id=subreview_id)
            details.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pricingsubdetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request,page_slug, review_id,subreview_id):
        try:
          details = Pricingdetails.objects.get(id=review_id)
        except Pricingdetails.DoesNotExist:
            return Response({'error': 'review id not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            page = Pricing.objects.get(slug=page_slug)
        except Pricing.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            details = Pricingsubdetails.objects.get(id=subreview_id)
            serializer = PricingsubdetailsSerializer(details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pricingsubdetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ServicesBlogPostView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ServicesBlogPostSerializer

    def get_blogpost(self, blog_slug):
        try:
            review = BlogPost.objects.get(slug=blog_slug)
            return review
        except BlogPost.DoesNotExist:
            return None
    
    def get(self, request, page_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

        reviews = BlogPost.objects.filter(page=page)
        serializer = ServicesBlogPostSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, page_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ServicesBlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(page=page)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ServicessingleBlogPostView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ServicesBlogPostSerializer

    def get_blogpost(self, blog_slug):
        try:
            review = BlogPost.objects.get(slug=blog_slug)
            return review
        except BlogPost.DoesNotExist:
            return None


    def get(self, request, page_slug, blog_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
           reviews = BlogPost.objects.get(page=page,slug=blog_slug)
        except BlogPost.DoesNotExist:
            return Response({'error': 'BlogPost not found'}, status=status.HTTP_404_NOT_FOUND)
        print(reviews)
        serializer = ServicesBlogPostSerializer(reviews)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request,page_slug, blog_slug):
        review = self.get_blogpost(blog_slug)
        if not review:
            return Response({'error': 'BlogPost not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServicesBlogPostSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,page_slug, blog_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

        review = self.get_blogpost(blog_slug)
        if not review:
            return Response({'error': 'BlogPost not found'}, status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OurworkprojectView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = OurworkprojectSerializer

    def get_work(self, work_slug):
        try:
            review = Ourworkproject.objects.get(slug=work_slug)
            return review
        except Ourworkproject.DoesNotExist:
            return None
    
    def get(self, request, page_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)

        reviews = Ourworkproject.objects.filter(page=page)
        serializer = OurworkprojectSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, page_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OurworkprojectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(page=page)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ServicessingleOurworkView(GenericAPIView):


    permission_classes = [IsAuthenticated]
    serializer_class = OurworkprojectSerializer

    def get_work(self, work_slug):
        try:
            review = Ourworkproject.objects.get(slug=work_slug)
            return review
        except Ourworkproject.DoesNotExist:
            return None


    def get(self, request, page_slug, work_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
          reviews = Ourworkproject.objects.get(page=page,slug=work_slug)
        except Ourworkproject.DoesNotExist:
            return Response({'error': 'Ourworkproject not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OurworkprojectSerializer(reviews)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request,page_slug, work_slug):
        review = self.get_work(work_slug)
        if not review:
            return Response({'error': 'workproject not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OurworkprojectSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,page_slug, work_slug):
        try:
            page = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
        review = self.get_work(work_slug)
        if not review:
            return Response({'error': 'workproject not found'}, status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogauthorView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BlogauthorSerializer

    def get(self, request):
        details = Blogauthor.objects.all()
        serializer = BlogauthorSerializer(details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogauthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogauthorUpdateView(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = BlogauthorSerializer

    def get(self, request ,author_id):
        try:
          details = Blogauthor.objects.get(id=author_id)
        except Blogauthor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogauthorSerializer(details)
        return Response(serializer.data)

    def delete(self, request, author_id):
        try:
            details = Blogauthor.objects.get(id=author_id)
            details.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Blogauthor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, author_id):
        try:
            details = Blogauthor.objects.get(id=author_id)
            serializer = BlogauthorSerializer(details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Blogauthor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TagView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer

    
    def get(self, request):
        details = Tag.objects.all()
        serializer = TagSerializer(details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagUpdateView(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer

    def get(self, request,tag_id):
        try:
            details = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return Response({'error': 'Tag Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TagSerializer(details)
        return Response(serializer.data)

    def delete(self, request, tag_id):
        try:
            details = Tag.objects.get(id=tag_id)
            details.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, tag_id):
        try:
            details = Tag.objects.get(id=tag_id)
            serializer = TagSerializer(details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tag.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class homeView(GenericAPIView):

    serializer_class = HomeSerializer

    def get(self, request):
        try:
            blogs = Homepage.objects.first()
        except Homepage.DoesNotExist:
            return Response({'error': 'please create a homepage template in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HomeSerializer(blogs)
        return Response(serializer.data)

class pricingView(GenericAPIView):

    serializer_class = PricingUserSerializer

    def get(self, request):
        try:
            blogs = Pricing.objects.first()
        except Pricing.DoesNotExist:
            return Response({'error': 'please create a Pricingpage template in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PricingUserSerializer(blogs)
        return Response(serializer.data)

class WhyususerView(GenericAPIView):

    serializer_class = WhyusUserSerializer

    def get(self, request):
        try:
            blogs = Whyus.objects.first()
        except Whyus.DoesNotExist:
            return Response({'error': 'please create a Whyus template in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WhyusUserSerializer(blogs)
        return Response(serializer.data)


class OurworkuserView(GenericAPIView):

    serializer_class = OurworkUserSerializer

    def get(self, request):
        try:
            blogs = Ourwork.objects.first()
        except Ourwork.DoesNotExist:
            return Response({'error': 'please create a Ourwork template in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OurworkUserSerializer(blogs)
        return Response(serializer.data)




from rest_framework import generics
from .serializers import WorkresultSerializer
from rest_framework.pagination import LimitOffsetPagination

class ShowMorePagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 2

class OurworkresultView(generics.ListAPIView):
    serializer_class = WorkresultSerializer
    pagination_class = ShowMorePagination

    def get_queryset(self):
        slug = self.kwargs.get('page_slug')
        if slug:
            return Ourworkproject.objects.filter(page__slug=slug)
        else:
            return Ourworkproject.objects.all()


# class CustomPagination(PageNumberPagination):
#     page_size = 6

class OurworkallresultView(generics.ListAPIView):
    serializer_class = WorkresultSerializer
    queryset = Ourworkproject.objects.all()
    pagination_class = ShowMorePagination

class OurworkresultsingleView(generics.ListAPIView):
    serializer_class = WorkresultSerializer

    def get_queryset(self):
        slug = self.kwargs.get('page_slug')
        work = self.kwargs.get('work_slug')
        return Ourworkproject.objects.filter(slug=work, page__slug=slug)
    


class OurworkresultsinglenextAPIView(GenericAPIView):

    serializer_class = WorkresultSerializer

    def get(self, request,page_slug, work_slug):
        try:
            current_blog = Ourworkproject.objects.get(slug=work_slug).id
            next_blog = Ourworkproject.objects.filter(id__gt=current_blog,page__slug=page_slug).first()
            if next_blog is not None:
                serializer = WorkresultSerializer(next_blog)
                return Response(serializer.data)
            else:
                return Response(status=404)
        except Ourworkproject.DoesNotExist:
            return Response(status=404)

class OurworkresultsinglepreviousView(GenericAPIView):

    serializer_class = WorkresultSerializer

    def get(self, request,page_slug, work_slug):
        try:
            current_id = Ourworkproject.objects.get(slug=work_slug).id
            # current_blog = Ourworkproject.objects.get(id=blog_id,,page__slug=page_slug)
            previous_blog = Ourworkproject.objects.filter(id__lt=current_id,page__slug=page_slug).last()
            if previous_blog is not None:
                serializer = WorkresultSerializer(previous_blog)
                return Response(serializer.data)
            else:
                return Response(status=404)
        except Ourworkproject.DoesNotExist:
            return Response(status=404)



class BloguserView(GenericAPIView):

    serializer_class = BlogTimepassUserSerializer

    def get(self, request):
        try:
            blogs = Blogs.objects.first()
        except Blogs.DoesNotExist:
            return Response({'error': 'please create a Blogs template in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogTimepassUserSerializer(blogs)
        return Response(serializer.data)

# PageHomeblogSerializer  BlogTimepassUserSerializer  BlogUserSerializer
class allBloguserView(generics.ListAPIView):
    serializer_class = blogsingleSerializer
    queryset = BlogPost.objects.all()
    pagination_class = ShowMorePagination

class BlogbycategoryView(GenericAPIView):

    serializer_class = PageblogSerializer

    def get(self, request,page_slug):
        try:
            blogs = Page.objects.filter(slug=page_slug)
            # first_three_blogs = blogs[:3]
        except Page.DoesNotExist:
            return Response({'error': 'please create a Page category in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PageblogSerializer(blogs, many=True)
        return Response(serializer.data)


class SingleblogView(GenericAPIView):

    serializer_class = blogsingleSerializer

    def get(self, request,page_slug):
        try:
            blogs = BlogPost.objects.get(slug=page_slug)
        except BlogPost.DoesNotExist:
            return Response({'error': 'please create a BlogPost in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = blogsingleSerializer(blogs)
        return Response(serializer.data)

class ServicesUserpageView(GenericAPIView):

    serializer_class = ServicesuserSerializer

    def get(self, request,page_slug):
        try:
            blogs = Page.objects.get(slug=page_slug)
        except Page.DoesNotExist:
            return Response({'error': 'please create a Page in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServicesuserSerializer(blogs)
        return Response(serializer.data)







##########################################################################


class BookacallView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BookacallSerializer

    def get(self, request):
        try:
            ourwork = Bookacall.objects.first()
        except Bookacall.DoesNotExist:
            ourwork = Bookacall.objects.create()

        serializer = BookacallSerializer(ourwork)
        return Response(serializer.data)

    def put(self, request):
        try:
            ourwork = Bookacall.objects.first()
        except Bookacall.DoesNotExist:
            return Response({'error': 'Bookacall page is not created'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookacallSerializer(ourwork, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookacallsectiononeView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BookacallsectiononeSerializer

    def get(self, request, page_slug):
        try:
            section1 = Bookacallsectionone.objects.get(page__slug=page_slug)
        except Bookacallsectionone.DoesNotExist:
            try:
                page = Bookacall.objects.get(slug=page_slug)
            except Bookacall.DoesNotExist:
                return Response({'error': 'Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Bookacallsectionone.objects.create(page=page)

        serializer = BookacallsectiononeSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Bookacallsectionone.objects.get(page__slug=page_slug)
        except Bookacallsectionone.DoesNotExist:
            return Response({'error': 'Bookacallsectionone object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookacallsectiononeSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookacallsectiontwoView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BookacallsectiontwoSerializer

    def get(self, request, page_slug):
        try:
            section1 = Bookacallsectiontwo.objects.get(page__slug=page_slug)
        except Bookacallsectiontwo.DoesNotExist:
            try:
                page = Bookacall.objects.get(slug=page_slug)
            except Bookacall.DoesNotExist:
                return Response({'error': 'Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)

            section1 = Bookacallsectiontwo.objects.create(page=page)

        serializer = BookacallsectiontwoSerializer(section1)
        return Response(serializer.data)

    def put(self, request, page_slug):
        try:
            section1 = Bookacallsectiontwo.objects.get(page__slug=page_slug)
        except Bookacallsectiontwo.DoesNotExist:
            return Response({'error': 'Bookacallsectiontwo object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookacallsectiontwoSerializer(section1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookacallSlidersection1View(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = BookacallSlidersection1Serializer

#     def get_image(self, image_id):
#         try:
#             review = BookacallSlidersection1.objects.get(id=image_id)
#             return review
#         except BookacallSlidersection1.DoesNotExist:
#             return None
    
#     def get(self, request, page_slug):
#         try:
#             page = Bookacall.objects.get(slug=page_slug)
#         except Bookacall.DoesNotExist:
#             return Response({'error': 'Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)

#         images = BookacallSlidersection1.objects.filter(page=page)
#         serializer = BookacallSlidersection1Serializer(images, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, page_slug):
#         try:
#             page = Bookacall.objects.get(slug=page_slug)
#         except Bookacall.DoesNotExist:
#             return Response({'error':  ' Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = BookacallSlidersection1Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(page=page)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BookacallUpdateSlidersection1View(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = BookacallSlidersection1Serializer

#     def get_image(self, image_id):
#         try:
#             review = BookacallSlidersection1.objects.get(id=image_id)
#             return review
#         except BookacallSlidersection1.DoesNotExist:
#             return None
    
#     def get(self, request, page_slug , image_id):
#         try:
#             page = Bookacall.objects.get(slug=page_slug)
#         except Bookacall.DoesNotExist:
#             return Response({'error': 'Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         image = self.get_image(image_id)
#         if image is None:
#             return Response({'error': 'image not found'}, status=status.HTTP_404_NOT_FOUND)
#         try:
#           images = BookacallSlidersection2.objects.filter(page=page,id=image_id)
#         except ObjectDoesNotExist:
#             return Response({'error': 'image id not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BookacallSlidersection1Serializer(images,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request,page_slug, image_id):
#         try:
#             page = Bookacall.objects.get(slug=page_slug)
#         except Bookacall.DoesNotExist:
#             return Response({'error': 'Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         image = self.get_image(image_id)
#         if image is None:
#             return Response({'error': 'image not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = BookacallSlidersection1Serializer(image, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request,page_slug, image_id):
#         try:
#             page = Bookacall.objects.get(slug=page_slug)
#         except Bookacall.DoesNotExist:
#             return Response({'error': 'Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         image = self.get_image(image_id)
#         if image is None:
#             return Response({'error': 'image not found'}, status=status.HTTP_404_NOT_FOUND)

#         image.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class BookacallSlidersection2View(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = BookacallSlidersection2Serializer


#     def get_image(self, image_id):
#         try:
#             review = BookacallSlidersection2.objects.get(id=image_id)
#             return review
#         except BookacallSlidersection2.DoesNotExist:
#             return None
    
#     def get(self, request, page_slug):
#         try:
#             page = Bookacall.objects.get(slug=page_slug)
#         except Bookacall.DoesNotExist:
#             return Response({'error': ' Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)

#         images = BookacallSlidersection2.objects.filter(page=page)
#         serializer = BookacallSlidersection2Serializer(images, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, page_slug):
#         try:
#             page = Bookacall.objects.get(slug=page_slug)
#         except Bookacall.DoesNotExist:
#             return Response({'error': 'Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = BookacallSlidersection2Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(page=page)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookacallUpdateSlidersection2View(GenericAPIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = BookacallSlidersection2Serializer

#     def get_image(self, image_id):
#         try:
#             review = BookacallSlidersection2.objects.get(id=image_id)
#             return review
#         except BookacallSlidersection2.DoesNotExist:
#             return None
    
#     def get(self, request, page_slug,image_id):
#         try:
#             page = Bookacall.objects.get(slug=page_slug)
#         except Bookacall.DoesNotExist:
#             return Response({'error': ' Bookacall Page not found'}, status=status.HTTP_404_NOT_FOUND)
#         image = self.get_image(image_id)
#         if image is None:
#             return Response({'error': 'image not found'}, status=status.HTTP_404_NOT_FOUND)
#         try:
#           images = BookacallSlidersection2.objects.filter(page=page,id=image_id)
#         except ObjectDoesNotExist:
#             return Response({'error': 'image id not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BookacallSlidersection2Serializer(images,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request,page_slug, image_id):
#         image = self.get_image(image_id)
#         if image is None:
#             return Response({'error': 'image not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = BookacallSlidersection2Serializer(image, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request,page_slug, image_id):
#         image = self.get_image(image_id)
#         if image is None:
#             return Response({'error': 'image not found'}, status=status.HTTP_404_NOT_FOUND)

#         image.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class bookacalluserView(GenericAPIView):
    def get(self, request):
        try:
            blogs = Bookacall.objects.first()
        except Bookacall.DoesNotExist:
            return Response({'error': 'please create a Bookacall template in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = bookcallUserSerializer(blogs)
        return Response(serializer.data)


class UserSocialView(GenericAPIView):

    serializer_class = SocialSerializer

    # def get_image(self, image_id):
    #     try:
    #         review = BookacallSlidersection2.objects.get(id=image_id)
    #         return review
    #     except BookacallSlidersection2.DoesNotExist:
    #         return None
    
    def get(self, request):
        try:
            page = Social.objects.all()
        except Social.DoesNotExist:
            return Response({'error': ' Social Page not found'}, status=status.HTTP_404_NOT_FOUND)

        # images = BookacallSlidersection2.objects.filter(page=page)
        serializer = SocialSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SocialView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = SocialSerializer

    # def get_image(self, image_id):
    #     try:
    #         review = BookacallSlidersection2.objects.get(id=image_id)
    #         return review
    #     except BookacallSlidersection2.DoesNotExist:
    #         return None
    
    def get(self, request):
        try:
            page = Social.objects.all()
        except Social.DoesNotExist:
            return Response({'error': ' Social Page not found'}, status=status.HTTP_404_NOT_FOUND)

        # images = BookacallSlidersection2.objects.filter(page=page)
        serializer = SocialSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
       
        serializer = SocialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SocialupdateView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = SocialSerializer

    def get_image(self, social_id):
        try:
            review = Social.objects.get(id=social_id)
            return review
        except Social.DoesNotExist:
            return None
    
    def get(self, request,social_id):
        try:
            page = Social.objects.get(id=social_id)
        except Social.DoesNotExist:
            return Response({'error': ' Social Page not found'}, status=status.HTTP_404_NOT_FOUND)

        # images = BookacallSlidersection2.objects.filter(page=page,id=image_id)
        serializer = SocialSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, social_id):
        image = self.get_image(social_id)
        if image is None:
            return Response({'error': 'Social not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SocialSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,social_id):
        image = self.get_image(social_id)
        if image is None:
            return Response({'error': 'Social not found'}, status=status.HTTP_404_NOT_FOUND)

        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IsPostOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'


class EmailView(GenericAPIView):

    permission_classes = [IsAuthenticated | IsPostOnly]
    serializer_class = EmailSerializer

    def get(self, request):
        try:
            page = Emailinput.objects.all()
        except Emailinput.DoesNotExist:
            return Response({'error': ' Emailinput Page not found'}, status=status.HTTP_404_NOT_FOUND)

        # images = BookacallSlidersection2.objects.filter(page=page)
        serializer = EmailSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
       
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class authornameview(GenericAPIView):
    def get(self, request,author_name):
        try:
          author = Blogauthor.objects.get(slug=author_name)  # Replace `author_id` with the actual ID of the author
        #   blog_posts = author.blogpostauthor.all()  # Retrieve all blog posts of the author
        except Blogauthor.DoesNotExist:
            return Response({'error': 'please Blogauthor template in Dashboard'}, status=status.HTTP_404_NOT_FOUND)

        serializer = blogpageauthorSerializer(author)
        return Response(serializer.data)


# class BlogbyauthorView(GenericAPIView):
#     def get(self, request,author_name):
#         try:
#           author = BlogPost.objects.filter(author__slug=author_name)  # Replace `author_id` with the actual ID of the author
#         #   blog_posts = author.blogpostauthor.all()  # Retrieve all blog posts of the author
#         except BlogPost.DoesNotExist:
#             return Response({'error': 'No blog for this particular author'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = blogpageauthorSerializer(author)
#         return Response(serializer.data)


class BlogbyauthorView(generics.ListAPIView):
    serializer_class = blogsingleSerializer
    pagination_class = ShowMorePagination

    def get_queryset(self):
        slug = self.kwargs.get('author_name')
        return BlogPost.objects.filter(Postauthor__slug=slug)



class authordetailsView(GenericAPIView):
    
    def get(self, request,author_name):
        try:
            page = Blogauthor.objects.get(slug=author_name)
        except Blogauthor.DoesNotExist:
            return Response({'error': 'author with this name does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # images = BookacallSlidersection2.objects.filter(page=page)
        serializer = authordetailsSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogbytagView(generics.ListAPIView):
    serializer_class = blogsingleSerializer
    pagination_class = ShowMorePagination

    def get_queryset(self):
        slug = self.kwargs.get('tag_slug')
        return BlogPost.objects.filter(tag__slug=slug)


class tagdetailsView(GenericAPIView):
    
    def get(self, request,tag_name):
        try:
            page = Tag.objects.get(slug=tag_name)
        except Tag.DoesNotExist:
            return Response({'error': 'Tag with this name does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # images = BookacallSlidersection2.objects.filter(page=page)
        serializer = TagSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# from rest_framework.views import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.authtoken.models import Token

class MyAPIView(GenericAPIView):
    @swagger_auto_schema(security=[{"Token": []}])
    def post(self, request):
        # Extract the token from the request
        token_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

        # Perform authentication and authorization checks
        is_authenticated = False
        is_authorized = False

        # Perform token authentication
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            is_authenticated = True
        except Token.DoesNotExist:
            pass

        # Perform your authorization logic
        # Example: Check if the authenticated user has the necessary permissions
        if is_authenticated and user.has_perm('myapp.can_post'):
            is_authorized = True

        # If the user is not authenticated or authorized, return an error response
        if not is_authenticated or not is_authorized:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        # Process the request data
        # Your request processing code here

        # Return a response
        return Response({'message': 'Success'})

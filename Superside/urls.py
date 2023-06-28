"""
URL configuration for Britishbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import navigation.signals
from navigation.api.views import (
    ImageUploadView, HeaderView, MenuView, SubMenuView, FooterView, SectiontwoView, SectionfourView,OurworkuserView,OurworkresultsingleView,ServicesUserpageView,PricingUpdateFaqView,authordetailsView,
    SectiononeView, VideoUploadView, SectionthreeView, DetailsView, HomepageReviewView, PageView,WhyususerView,OurworkallresultView,bookacalluserView,HomepageUpdateSlidersection2View,authornameview,ImageUpdateUploadView,
    PagelistView, ServicessectiononeView, ServicessectiontwoView, ServicessectionThreeView,homepageView,homeView,BloguserView,SingleblogView,BlogbycategoryView,PricingUpdatedetailsView,DetailsUpdateView,PricingUpdatesubdetailsView,allBloguserView,BlogbytagView,SectionfiveView,singlereviewView,sectionsixView, FaqView, ServicessectionsixView, ServicessectionsevenView,servicesview,OurworkresultView,HomepageSlidersection1updateView,HomepageUpdateReviewView,FaqUpdateView,SocialupdateView,tagdetailsView,UserFooterView,UsernavbarView,
    BookacallView,BookacallsectiononeView,BookacallsectiontwoView,HomepageSlidersection1View,HomepageSlidersection2View,OurworkresultsinglepreviousView,OurworkresultsinglenextAPIView,BlogbyauthorView,UserHeaderView,UserHomepageSlidersection1View,UserHomepageSlidersection2View,UserHomepageReviewView,
    OurworksectiononeView, OurworksectiontwoView, OurworkView, BlogsView, BlogssectiononeView,OurworkprojectView,ServicessingleOurworkView,BlogauthorView,BlogauthorUpdateView,TagView,TagUpdateView,pricingView,EmailView,VideoUpdateUploadView,
    BlogssectiontwoView, BlogssectionthreeView, BlogssectionfourView, WhyussectiontwoView,WhyussectionthreeView,WhyussectionfourView,WhyussectionfiveView,WhyussectionsixView,WhyusView,WhyussectionsevenView,SocialView,MenuUpdateView,SubMenuUpdateView,
    PricingdetailsView,PricingFaqView,PricingsectionfourView,PricingsectionthreeView,PricingView,PricingsectiontwoView,PricingsectiononeView,PricingsubdetailsView,ServicesBlogPostView,ServicessingleBlogPostView,UserSocialView
)
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Superside Api",
        default_version="v1",
        description="Api of Superside ",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="dolikemathewalex@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path('api/account/', include('accounts.api.urls')),
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('upload/<int:image_id>/', ImageUpdateUploadView.as_view(), name='image-delete'),
    path('upload/video/', VideoUploadView.as_view(), name='video-upload'),
    path('upload/video/<int:video_id>/', VideoUpdateUploadView.as_view(), name='Video-delete'),
    path('header/', UserHeaderView.as_view()),
    path('navbar/', UsernavbarView.as_view()),
    path('footer/', UserFooterView.as_view()),
    path('social/', UserSocialView.as_view()),##approved
    path('dashboard/header/', HeaderView.as_view()),
    path('dashboard/menu/', MenuView.as_view()),
    path('dashboard/menu/<int:menu_id>/', MenuUpdateView.as_view()),
    path('dashboard/menu/<int:menu_id>/submenu/', SubMenuView.as_view()),
    path('dashboard/menu/<int:menu_id>/submenu/<int:submenu_id>/', SubMenuUpdateView.as_view()),
    path('dashboard/footer/', FooterView.as_view()),
    path('homepage/', homeView.as_view()),
    path('servicepage/<slug:page_slug>/', ServicesUserpageView.as_view(),name='servicespages'),
    path('pricing/', pricingView.as_view()),
    path('whyus/', WhyususerView.as_view()),
    path('ourwork/', OurworkuserView.as_view()),
    path('bookacall/', bookacalluserView.as_view()),
    path('ourwork/all/', OurworkallresultView.as_view(),name='ourworkallresult'),
    path('ourwork/all/<slug:page_slug>/', OurworkresultView.as_view(),name='ourworkresult'),
    path('ourwork/all/<slug:page_slug>/<slug:work_slug>/', OurworkresultsingleView.as_view(),name='ourworksingle'),
    path('ourwork/all/<slug:page_slug>/<slug:work_slug>/next', OurworkresultsinglenextAPIView.as_view(),name='ourworksingle-next'),
    path('ourwork/all/<slug:page_slug>/<slug:work_slug>/previous', OurworkresultsinglepreviousView.as_view(),name='ourworksingle-previous'),
    path('blogs/', BloguserView.as_view()),
    path('blogs/all/', allBloguserView.as_view()),
    path('blogs/category/<slug:page_slug>/', BlogbycategoryView.as_view(),name='blogbycategory'),
    path('blogs/tags/<slug:tag_slug>/', BlogbytagView.as_view(),name='blogbytag'),
    path('blogs/<slug:page_slug>/', SingleblogView.as_view(),name='singleblog'),
    path('blogs/author/<slug:author_name>/', authornameview.as_view(),name='authorname'),
    path('blogs/all/author/<slug:author_name>/', BlogbyauthorView.as_view(),name='blogbyauthorauthorname'),
    path('author/<slug:author_name>/', authordetailsView.as_view(),name='authordetails'),
    path('slider1/', UserHomepageSlidersection1View.as_view(),name='authordetails'),
    path('slider2/', UserHomepageSlidersection2View.as_view(),name='authordetails'),
    path('review/', UserHomepageReviewView.as_view(),name='authordetails'),
    path('tag/<slug:tag_name>/', tagdetailsView.as_view(),name='tagdetails'),
    # path('homepage/<slug:page_slug>/', servicesview.as_view(),name='servicespages'),
    path('dashboard/subscriberemail/', EmailView.as_view(),name='subscriberemail'),#approved
    path('dashboard/social/', SocialView.as_view(),name='socialmedia'),##approved
    path('dashboard/social/<int:social_id>/', SocialupdateView.as_view(),name='socialmedia-update'),#approved
    path('dashboard/homepage/', homepageView.as_view(),name='homepage'),
    path('dashboard/homepage/<slug:page_slug>/sectiontwo/', SectiontwoView.as_view(),name='homepagesectiontwo'),
    path('dashboard/homepage/<slug:page_slug>/sectionfour/', SectionfourView.as_view(),name='homepagesectionfour'),
    path('dashboard/homepage/<slug:page_slug>/sectionone/', SectiononeView.as_view(),name='homepagesectionone'),
    path('dashboard/homepage/<slug:page_slug>/sectionthree/', SectionthreeView.as_view(),name='homepagesectionthree'),
    path('dashboard/imageslider1/', HomepageSlidersection1View.as_view(),name='HomepageSlidersection1'),
    path('dashboard/imageslider1/<int:image_id>/', HomepageSlidersection1updateView.as_view(), name='HomepageSlidersection1-update'),
    path('dashboard/imageslider2/', HomepageSlidersection2View.as_view(),name='HomepageSlidersection2'),
    path('dashboard/imageslider2/<int:image_id>/', HomepageUpdateSlidersection2View.as_view(), name='HomepageSlidersection2-update'),
    path('dashboard/homepage/<slug:page_slug>/details/', DetailsView.as_view(),name='homepagedetailsection'),
    path('dashboard/homepage/<slug:page_slug>/sectionfive/', SectionfiveView.as_view(),name='homepagesectionfive'),
    path('dashboard/homepage/<slug:page_slug>/reviewsingle/', singlereviewView.as_view(),name='homepagesinglereview'),
    path('dashboard/homepage/<slug:page_slug>/sectionsix/', sectionsixView.as_view(),name='homepagesectionsix'),
    path('dashboard/homepage/<slug:page_slug>/details/<int:details_id>/', DetailsUpdateView.as_view(),name='homepagedetailsection-update'),
    path('dashboard/reviews/', HomepageReviewView.as_view(),name='homepagereviewsection'),
    path('dashboard/reviews/<int:review_id>/', HomepageUpdateReviewView.as_view(),name='homepagereviewsection-update'),
    path('dashboard/pricing/', PricingView.as_view(),name='pricing'),
    path('dashboard/pricing/<slug:page_slug>/sectionone/', PricingsectiononeView.as_view(),name='Pricingsectionone'),
    path('dashboard/pricing/<slug:page_slug>/sectiontwo/', PricingsectiontwoView.as_view(),name='Pricingsectiontwo'),
    path('dashboard/pricing/<slug:page_slug>/sectionthree/', PricingsectionthreeView.as_view(),name='Pricingsectionthree'),
    path('dashboard/pricing/<slug:page_slug>/sectionfour/', PricingsectionfourView.as_view(),name='Pricingsectionfour'),
    path('dashboard/pricing/<slug:page_slug>/pricingdetails/', PricingdetailsView.as_view(),name='Pricingdetails'),
    path('dashboard/pricing/<slug:page_slug>/pricingdetails/<int:review_id>/', PricingUpdatedetailsView.as_view(),name='Pricingdetails-update'),
    path('dashboard/pricing/<slug:page_slug>/pricingdetails/<int:review_id>/subdetails/', PricingsubdetailsView.as_view(),name='Pricingsubdetails'),
    path('dashboard/pricing/<slug:page_slug>/pricingdetails/<int:review_id>/subdetails/<int:subreview_id>/', PricingUpdatesubdetailsView.as_view(),name='Pricingsubdetails-update'),
    # path('dashboard/pricing/<slug:page_slug>/review/', PricinguserreviewView.as_view(),name='Pricinguserreview'),
    # path('dashboard/pricing/<slug:page_slug>/review/<int:review_id>/', PricinguserUpdatereviewView.as_view(),name='Pricinguserreview-update'),
    path('dashboard/pricing/<slug:page_slug>/faq/', PricingFaqView.as_view(),name='PricingFaq'),
    path('dashboard/pricing/<slug:page_slug>/faq/<int:review_id>/', PricingUpdateFaqView.as_view(),name='PricingFaq-update'),     
    path('dashboard/whyus/', WhyusView.as_view(),name='whyus'),
    path('dashboard/whyus/<slug:page_slug>/sectionone/', WhyussectionsevenView.as_view(),name='whyussectionone'),
    path('dashboard/whyus/<slug:page_slug>/sectiontwo/', WhyussectiontwoView.as_view(),name='whyussectiontwo'),
    path('dashboard/whyus/<slug:page_slug>/sectionthree/', WhyussectionthreeView.as_view(),name='whyussectionthree'),
    path('dashboard/whyus/<slug:page_slug>/sectionfour/', WhyussectionfourView.as_view(),name='whyussectionfour'),
    path('dashboard/whyus/<slug:page_slug>/sectionfive/', WhyussectionfiveView.as_view(),name='whyussectionfive'),
    path('dashboard/whyus/<slug:page_slug>/sectionsix/', WhyussectionsixView.as_view(),name='whyussectionsix'),
    # path('dashboard/whyus/<slug:page_slug>/review/', whyusReviewView.as_view(),name='whyusreview'),
    # path('dashboard/whyus/<slug:page_slug>/review/<int:review_id>/', whyusUpdateReviewView.as_view(),name='whyusreview-update'),
    path('dashboard/blogs/', BlogsView.as_view(),name='blogs'),
    path('dashboard/blogs/<slug:page_slug>/sectionone/', BlogssectiononeView.as_view(),name='blogsectionone'),
    path('dashboard/blogs/<slug:page_slug>/sectiontwo/', BlogssectiontwoView.as_view(),name='blogsectiontwo'),
    path('dashboard/blogs/<slug:page_slug>/sectionthree/', BlogssectionthreeView.as_view(),name='blogsectionthree'),
    path('dashboard/blogs/<slug:page_slug>/sectionfour/', BlogssectionfourView.as_view(),name='blogsectionfour'),
    path('dashboard/ourwork/', OurworkView.as_view(),name='ourwork'),
    path('dashboard/ourwork/<slug:page_slug>/sectionone/', OurworksectiononeView.as_view(),name='ourworksectionone'),
    path('dashboard/ourwork/<slug:page_slug>/sectiontwo/', OurworksectiontwoView.as_view(),name='ourworksectiontwo'),
    path('dashboard/pages/', PagelistView.as_view()),
    path('dashboard/pages/<slug:page_slug>/', PageView.as_view(), name='page'),
    path('dashboard/pages/<slug:page_slug>/sectionone/', ServicessectiononeView.as_view(), name='servicessectionone'),
    path('dashboard/pages/<slug:page_slug>/sectiontwo/', ServicessectiontwoView.as_view(), name='servicessectiontwo'),
    path('dashboard/pages/<slug:page_slug>/sectionthree/', ServicessectionThreeView.as_view(), name='servicessectionthree'),
    # path('dashboard/pages/<slug:page_slug>/reviews/', ServicesreviewView.as_view(), name='servicessectionreviews'),
    # path('dashboard/pages/<slug:page_slug>/reviews/<int:review_id>/', ServicesreviewUpdateView.as_view(), name='servicessectionreviews-update'),
    path('dashboard/pages/<slug:page_slug>/faq/', FaqView.as_view(), name='servicessectionfaq'),
    path('dashboard/pages/<slug:page_slug>/faq/<int:faq_id>/', FaqUpdateView.as_view(), name='servicessectionfaq-update'),
    path('dashboard/pages/<slug:page_slug>/sectionsix/', ServicessectionsixView.as_view(), name='servicessectionsix'),
    path('dashboard/pages/<slug:page_slug>/BlogPost/', ServicesBlogPostView.as_view(), name='servicesBlogPost'),
    path('dashboard/pages/<slug:page_slug>/BlogPost/<slug:blog_slug>/', ServicessingleBlogPostView.as_view(), name='servicesBlogPost-update'),
    path('dashboard/pages/<slug:page_slug>/ourwork/', OurworkprojectView.as_view(), name='servicesourwork'),
    path('dashboard/pages/<slug:page_slug>/ourwork/<slug:work_slug>/', ServicessingleOurworkView.as_view(), name='servicesourwork-update'),
    path('dashboard/pages/<slug:page_slug>/sectionseven/', ServicessectionsevenView.as_view(), name='servicessectionseven'),
    # path('dashboard/pages/<slug:page_slug>/sliderimage/', SlidersectionView.as_view(), name='sliderimage'),
    # path('dashboard/pages/<slug:page_slug>/sliderimage/<int:image_id>/', SlidersectionUpdateView.as_view(), name='sliderimage-update'),
    path('dashboard/blogauthors/', BlogauthorView.as_view(), name='addblogauthor'),#approved
    path('dashboard/blogauthors/<int:author_id>/', BlogauthorUpdateView.as_view(), name='addblogauthor-update'),#approved
    path('dashboard/blogtags/', TagView.as_view(), name='blogtags'),#approved
    path('dashboard/blogtags/<int:tag_id>/', TagUpdateView.as_view(), name='blogtags-update'),#approved
    path('dashboard/bookacall/', BookacallView.as_view(),name='bookacalldashboard'),
    path('dashboard/bookacall/<slug:page_slug>/sectionone/', BookacallsectiononeView.as_view(), name='bookacallsection1'),
    path('dashboard/bookacall/<slug:page_slug>/sectiontwo/', BookacallsectiontwoView.as_view(), name='bookacallsection2'),
    # path('dashboard/bookacall/<slug:page_slug>/sectionthree/', BookacallSlidersection1View.as_view(), name='bookacallslider1section'),
    # path('dashboard/bookacall/<slug:page_slug>/sectionthree/<int:image_id>/', BookacallUpdateSlidersection1View.as_view(), name='bookacallslider1section-update'),
    # path('dashboard/bookacall/<slug:page_slug>/sectionfour/', BookacallSlidersection2View.as_view(), name='bookacallslider2section'),
    # path('dashboard/bookacall/<slug:page_slug>/sectionfour/<int:image_id>/', BookacallUpdateSlidersection2View.as_view(), name='bookacallslider2section-update'),
    path('ckeditor/', include('ckeditor_uploader.urls')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from rest_framework import serializers
from django.urls import reverse

from navigation.models import ( 
    MediaBucket,Header,Menu,SubMenu,Footer,Sectiontwo,Sectionfour,Sectionone,VideoBucket,Sectionthree,Details,Pricingsubdetails,
    Page,Servicessectionone,Servicessectiontwo,ServicessectionThree,Faq,Servicessectionsix,Servicessectionseven,Pricingdetails,Emailinput,Social,Ourwork,Ourworksectionone,Ourworksectiontwo,Blogs,Blogsectionone,Blogsectiontwo,Blogsectionthree,Blogsectionfour,Pricingsectionfour,
    Whyus,Whyussectionseven,Whyussectionsix,Whyussectionfive,Whyussectionfour,Whyussectionthree,Whyussectionfour,Whyussectionthree,Homepage,Sectionfive,Singlereview,Sectionsix,
    Bookacall,Bookacallsectionone,Bookacallsectiontwo,CommonSlidersection2,CommonReview,CommonSlidersection1,
    Whyussectiontwo,PricingFaq,Pricingsectionthree,Pricingsectiontwo,Pricingsectionone,Pricing,BlogPost,Tag,Blogauthor,Ourworkproject
)


class MediaBucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaBucket
        fields = '__all__'

class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    sub_menu = SubMenuSerializer(many=True, read_only=True)
    class Meta:
        model = Menu
        fields = '__all__'

class HeaderSerializer(serializers.ModelSerializer):
    header = MenuSerializer(read_only=True)
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, Header):
        if Header.headerlogo:
            return Header.headerlogo.image.url
        return None

    class Meta:
        model = Header
        fields = ['id', 'headerlogo', 'photo_url', 'header']


class FooterSerializer(serializers.ModelSerializer):

      class Meta:
        model = Footer
        fields = '__all__'

# data_dict = {
#     "text1": "Value 1",
#     "text2": "Value 2",
#     "text3": "Value 3",
#     "text4": "Value 4",
#     "text5": [
#         {
#             "text6": "Value 6",
#             "text7": "Value 7",
#             "text8": "Value 8",
#         },
#         {
#             "text9": "Value 9",
#             "text10": "Value 10",
#             "text11": "Value 11",
#         },
#         {
#             "text10": "Value 10",
#             "text11": "Value 11",
#             "text12": "Value 12",
#         },
#         {
#             "text13": "Value 13",
#             "text14": "Value 14",
#             "text15": "Value 15",
#         },
#     ],
# }

class SectiontwoSerializer(serializers.ModelSerializer):


        def to_representation(self, instance):
            representation = super().to_representation(instance)
            data_dict = {
                "text1": representation.get("text1"),
                "text2": representation.get("text2"),
                "text3": representation.get("text3"),
                "Factcontent": [
                    {
                        "subTitle1": representation.get("text4"),
                        "title1": representation.get("text5"),
                        "desc1": representation.get("text6"),
                    },
                    {
                        "subTitle2": representation.get("text7"),
                        "title2": representation.get("text8"),
                        "desc2": representation.get("text9"),
                    },
                    {
                        "subTitle3": representation.get("text10"),
                        "title3": representation.get("text11"),
                        "desc3": representation.get("text12"),
                    },
                    {
                        "subTitle4": representation.get("text13"),
                        "title4": representation.get("text14"),
                        "desc4": representation.get("text15"),
                    },
                ],
            }
            return data_dict


        class Meta:
            model = Sectiontwo
            fields = '__all__'




class SectionfourSerializer(serializers.ModelSerializer):
    # sectionfourimage1_path = serializers.SerializerMethodField()
    # sectionfourimage2_path = serializers.SerializerMethodField()
    # sectionfourimage3_path = serializers.SerializerMethodField()
    # sectionfourimage4_path = serializers.SerializerMethodField()
    # sectionfourimage5_path = serializers.SerializerMethodField()

    # def get_sectionfourimage1_path(self, obj):
    #     if obj.sectionfourimage1:
    #         return obj.sectionfourimage1.image.url
    #     return None

    # def get_sectionfourimage2_path(self, obj):
    #     if obj.sectionfourimage2:
    #         return obj.sectionfourimage2.image.url
    #     return None

    # def get_sectionfourimage3_path(self, obj):
    #     if obj.sectionfourimage3:
    #         return obj.sectionfourimage3.image.url
    #     return None

    # def get_sectionfourimage4_path(self, obj):
    #     if obj.sectionfourimage4:
    #         return obj.sectionfourimage4.image.url
    #     return None

    # def get_sectionfourimage5_path(self, obj):
    #     if obj.sectionfourimage5:
    #         return obj.sectionfourimage5.image.url
    #     return None

    class Meta:
        model = Sectionfour
        fields = '__all__'


class singlereviewSerializer(serializers.ModelSerializer):
    # sectionfourimage1_path = serializers.SerializerMethodField()
    # sectionfourimage2_path = serializers.SerializerMethodField()
    # sectionfourimage3_path = serializers.SerializerMethodField()
    # sectionfourimage4_path = serializers.SerializerMethodField()
    # sectionfourimage5_path = serializers.SerializerMethodField()

    # def get_sectionfourimage1_path(self, obj):
    #     if obj.sectionfourimage1:
    #         return obj.sectionfourimage1.image.url
    #     return None

    # def get_sectionfourimage2_path(self, obj):
    #     if obj.sectionfourimage2:
    #         return obj.sectionfourimage2.image.url
    #     return None

    # def get_sectionfourimage3_path(self, obj):
    #     if obj.sectionfourimage3:
    #         return obj.sectionfourimage3.image.url
    #     return None

    # def get_sectionfourimage4_path(self, obj):
    #     if obj.sectionfourimage4:
    #         return obj.sectionfourimage4.image.url
    #     return None

    # def get_sectionfourimage5_path(self, obj):
    #     if obj.sectionfourimage5:
    #         return obj.sectionfourimage5.image.url
    #     return None

    class Meta:
        model = Singlereview
        fields = '__all__'




class SectionfiveSerializer(serializers.ModelSerializer):
    sectionfiveimage1_path = serializers.SerializerMethodField()
    sectionfiveimage2_path = serializers.SerializerMethodField()
    sectionfiveimage3_path = serializers.SerializerMethodField()
    sectionfiveimage4_path = serializers.SerializerMethodField()


    def get_sectionfiveimage1_path(self, obj):
        if obj.sectionfiveimage1:
            return obj.sectionfiveimage1.image.url
        return None

    def get_sectionfiveimage2_path(self, obj):
        if obj.sectionfiveimage2:
            return obj.sectionfiveimage2.image.url
        return None

    def get_sectionfiveimage3_path(self, obj):
        if obj.sectionfiveimage3:
            return obj.sectionfiveimage3.image.url
        return None

    def get_sectionfiveimage4_path(self, obj):
        if obj.sectionfiveimage4:
            return obj.sectionfiveimage4.image.url
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        data_dict = {
            "sectionfiveheading": representation.get("sectionfiveheading"),
            "sectionfivesubheading": representation.get("sectionfivesubheading"),
            "content": [
                {
                    "sectionfiveimage1": self.get_sectionfiveimage1_path(instance),
                    "sectionfiveimage1details": representation.get("sectionfiveimage1details"),
                },
                {
                    "sectionfiveimage2": self.get_sectionfiveimage2_path(instance),
                    "sectionfiveimage2details": representation.get("sectionfiveimage2details"),
                },
                {
                    "sectionfiveimage3": self.get_sectionfiveimage3_path(instance),
                    "sectionfiveimage3details": representation.get("sectionfiveimage3details"),
                },
                {
                    "sectionfiveimage4": self.get_sectionfiveimage4_path(instance),
                    "sectionfiveimage4details": representation.get("sectionfiveimage4details"),
                },
            ],
        }
        return data_dict


    class Meta:
        model = Sectionfive
        fields = '__all__'

class SectionsixSerializer(serializers.ModelSerializer):
    sectionsiximage1_path = serializers.SerializerMethodField()
    sectionsiximage2_path = serializers.SerializerMethodField()



    def get_sectionfiveimage1_path(self, obj):
        if obj.sectionfiveimage1:
            return obj.sectionfiveimage1.image.url
        return None

    def get_sectionfiveimage2_path(self, obj):
        if obj.sectionfiveimage2:
            return obj.sectionfiveimage2.image.url
        return None


    class Meta:
        model = Sectionsix
        fields = '__all__'




class SectiononeSerializer(serializers.ModelSerializer):
    sectiononeimage1_path = serializers.SerializerMethodField()
    sectiononeimage2_path = serializers.SerializerMethodField()
    sectiononeimage3_path = serializers.SerializerMethodField()
    sectiononeimage4_path = serializers.SerializerMethodField()
    sectiononeimage5_path = serializers.SerializerMethodField()


    def get_sectiononeimage1_path(self, obj):
        if obj.sectiononeimage1:
            return obj.sectiononeimage1.image.url
        return None

    def get_sectiononeimage2_path(self, obj):
        if obj.sectiononeimage2:
            return obj.sectiononeimage2.image.url
        return None

    def get_sectiononeimage3_path(self, obj):
        if obj.sectiononeimage3:
            return obj.sectiononeimage3.image.url
        return None

    def get_sectiononeimage4_path(self, obj):
        if obj.sectiononeimage4:
            return obj.sectiononeimage4.image.url
        return None

    def get_sectiononeimage5_path(self, obj):
        if obj.sectiononeimage5:
            return obj.sectiononeimage5.image.url
        return None

    class Meta:
        model = Sectionone
        fields = '__all__'


class VideoBucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoBucket
        fields = '__all__'



class SectionthreeSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    def get_video_url(self, Sectionthree):
        if Sectionthree.sectionthreevideo:
            return Sectionthree.sectionthreevideo.video.url
        return None

    class Meta:
        model = Sectionthree
        fields = '__all__'


class DetailsSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, Details):
        if Details.detailsimage:
            return Details.detailsimage.image.url
        return None

    class Meta:
        model = Details
        fields = '__all__'


class HomepageReviewSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, CommonReview):
        if CommonReview.userphoto:
            return CommonReview.userphoto.image.url
        return None

    class Meta:
        model = CommonReview
        fields = '__all__'

class HomepageSlidersection1Serializer(serializers.ModelSerializer):
      sectiononeimage1_path = serializers.SerializerMethodField()


      def get_sectiononeimage1_path(self, obj):
         if obj.sliderimage:
            return obj.sliderimage.image.url
         return None

      class Meta:
            model = CommonSlidersection1
            fields = '__all__'

class HomepageSlidersection2Serializer(serializers.ModelSerializer):
      sectiononeimage1_path = serializers.SerializerMethodField()


      def get_sectiononeimage1_path(self, obj):
         if obj.sliderimage:
            return obj.sliderimage.image.url
         return None

      class Meta:
            model = CommonSlidersection2
            fields = '__all__'

class BlogauthorSerializer(serializers.ModelSerializer):
    blogauthordp_path = serializers.SerializerMethodField()
    authorblog_path = serializers.SerializerMethodField()

    def get_blogauthordp_path(self, obj):
        if obj.profilephoto:
            return obj.profilephoto.image.url
        return None

    def get_authorblog_path(self, obj):
        if obj.slug:
            return reverse('authorname',args=[obj.slug])
        return None

    class Meta:
        model = Blogauthor
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    tagblog_path = serializers.SerializerMethodField()


    def get_tagblog_path(self, obj):
        if obj.slug:
            return reverse('blogbytag',args=[obj.slug])
        return None

    class Meta:
        model = Tag
        fields = '__all__'

class ServicesBlogPostSerializer(serializers.ModelSerializer):
      blogthumbnailimg_path = serializers.SerializerMethodField()
      Postauthor = BlogauthorSerializer(read_only=True)
      tag = TagSerializer(many=True,read_only=True)



      def get_blogthumbnailimg_path(self, BlogPost):
          if BlogPost.thumbnail:
              return BlogPost.thumbnail.image.url
          return None

    #   def get_tags(self, blogpost):
    #       tags = BlogPost.tag.all()
    #       return TagSerializer(tags, many=True).data

      class Meta:
        model = BlogPost
        fields = '__all__'


class OurworkprojectSerializer(serializers.ModelSerializer):
      projectthumbnail_path = serializers.SerializerMethodField()



      def get_projectthumbnail_path(self, obj):
          if obj.projectthumbnail:
              return obj.projectthumbnail.image.url
          return None

      class Meta:
        model = Ourworkproject
        fields = '__all__'
        
class PageSerializer(serializers.ModelSerializer):

    pagethumbnail_path = serializers.SerializerMethodField()
    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Page):
        if Page.slug:
            return reverse('servicespages',args=[Page.slug])
        return None


    def get_pagethumbnail_path(self, Page):
        if Page.pageimg:
            return Page.pageimg.image.url
        return None

    class Meta:
        model = Page  
        fields = ['title','pageimg','discription','slug','pagethumbnail_path','page_url']




class HomeSerializer(serializers.ModelSerializer):

    Homepagesectionone = SectiononeSerializer(many=True, read_only=True)
    Homepagesectiontwo = SectiontwoSerializer(read_only=True)
    # HomepageSlidersection1 = HomepageSlidersection1Serializer(many=True,read_only=True)
    # HomepageSlidersection2 = HomepageSlidersection2Serializer(many=True,read_only=True)
    Homepagesectionthree = SectionthreeSerializer(many=True, read_only=True)
    Homepagesectionfour = SectionfourSerializer(many=True, read_only=True)
    Homepageservicepages = PageSerializer(many=True, read_only=True)
    Homepagedetails = DetailsSerializer(many=True, read_only=True)
    # Homepagereview = HomepageReviewSerializer(many=True, read_only=True)
    HomepageSectionsix = SectionsixSerializer(many=True, read_only=True)
    HomepageSectionfive = SectionfiveSerializer(many=True, read_only=True)
    HomepageSinglereview = singlereviewSerializer(many=True, read_only=True)




    class Meta:
        model = Homepage
        fields = '__all__'



class ServicessectiononeSerializer(serializers.ModelSerializer):
      sectiononeimage1_path = serializers.SerializerMethodField()
      sectiononeimage2_path = serializers.SerializerMethodField()
      sectiononeimage3_path = serializers.SerializerMethodField()



      def get_sectiononeimage1_path(self, obj):
         if obj.sectiontoneimage1:
            return obj.sectiontoneimage1.image.url
         return None

      def get_sectiononeimage2_path(self, obj):
         if obj.sectiontoneimage2:
            return obj.sectiontoneimage2.image.url
         return None

      def get_sectiononeimage3_path(self, obj):
         if obj.sectiontoneimage3:
            return obj.sectiontoneimage3.image.url
         return None


      class Meta:
         model = Servicessectionone
         fields = '__all__'

class ServicessectiontwoSerializer(serializers.ModelSerializer):
      sectiontwoimage2_path = serializers.SerializerMethodField()
      sectiontwoimage3_path = serializers.SerializerMethodField()
      video_url = serializers.SerializerMethodField()

      def get_video_url(self, obj):
          if obj.sectiontwovideo:
             return obj.sectiontwovideo.video.url
          return None


      def get_sectiontwoimage2_path(self, obj):
         if obj.sectiontwoimage:
            return obj.sectiontwoimage.image.url
         return None

      def get_sectiontwoimage3_path(self, obj):
         if obj.sectiontwocoverimage:
            return obj.sectiontwocoverimage.image.url
         return None


      class Meta:
         model = Servicessectiontwo
         fields = '__all__'


class ServicessectionThreeSerializer(serializers.ModelSerializer):


      class Meta:
         model = ServicessectionThree
         fields = '__all__'

# class ServicesreviewSerializer(serializers.ModelSerializer):
#     photo_url = serializers.SerializerMethodField()

#     def get_photo_url(self, Servicesreview):
#         if Servicesreview.userphoto:
#             return Servicesreview.userphoto.image.url
#         return None

#     class Meta:
#         model = Servicesreview
#         fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):


      class Meta:
         model = Faq
         fields = '__all__'

class ServicessectionsixSerializer(serializers.ModelSerializer):
      sectiontwoimage1_path = serializers.SerializerMethodField()
      sectiontwoimage2_path = serializers.SerializerMethodField()



      def get_sectiontwoimage1_path(self, obj):
         if obj.sectionsiximage1:
            return obj.sectionsiximage1.image.url
         return None

      def get_sectiontwoimage2_path(self, obj):
         if obj.sectionsiximage2:
            return obj.sectionsiximage2.image.url
         return None


      class Meta:
         model = Servicessectionsix
         fields = '__all__'

class ServicessectionsevenSerializer(serializers.ModelSerializer):
    sectiononeimage1_path = serializers.SerializerMethodField()
    sectiononeimage2_path = serializers.SerializerMethodField()
    sectiononeimage3_path = serializers.SerializerMethodField()
    sectiononeimage4_path = serializers.SerializerMethodField()
    sectiononeimage5_path = serializers.SerializerMethodField()
    sectiononeimage6_path = serializers.SerializerMethodField()



    def get_sectiononeimage1_path(self, obj):
        if obj.sectionsevenimage1:
            return obj.sectionsevenimage1.image.url
        return None

    def get_sectiononeimage2_path(self, obj):
        if obj.sectionsevenimage2:
            return obj.sectionsevenimage2.image.url
        return None

    def get_sectiononeimage3_path(self, obj):
        if obj.sectionsevenimage3:
            return obj.sectionsevenimage3.image.url
        return None

    def get_sectiononeimage4_path(self, obj):
        if obj.sectionsevenimage4:
            return obj.sectionsevenimage4.image.url
        return None

    def get_sectiononeimage5_path(self, obj):
        if obj.sectionsevenimage5:
            return obj.sectionsevenimage5.image.url
        return None
    
    def get_sectiononeimage6_path(self, obj):
        if obj.sectionsevenimage6:
            return obj.sectionsevenimage6.image.url
        return None

    class Meta:
        model = Servicessectionseven
        fields = '__all__'


# class SlidersectionSerializer(serializers.ModelSerializer):
#       sectiononeimage1_path = serializers.SerializerMethodField()


#       def get_sectiononeimage1_path(self, obj):
#          if obj.sliderimage:
#             return obj.sliderimage.image.url
#          return None

#       class Meta:
#             model = Slidersection
#             fields = '__all__'





class HomepageSerializer(serializers.ModelSerializer):

    # sectiononeservices = ServicessectiononeSerializer(many=True, read_only=True)
    # sectiontwoservices = ServicessectiontwoSerializer(many=True, read_only=True)
    # sectionthreeservices = ServicessectionThreeSerializer(many=True, read_only=True)
    # servicesreviewpage = ServicesreviewSerializer(many=True, read_only=True)
    # servicesfaq = FaqSerializer(many=True, read_only=True)
    # sectionsixservices = ServicessectionsixSerializer(many=True, read_only=True)
    # sectionsevenservices = SectionsevenSerializer(many=True, read_only=True)
    # slidersection = SlidersectionSerializer(many=True, read_only=True)



    section1_url = serializers.SerializerMethodField()
    section2_url = serializers.SerializerMethodField()
    section3_url = serializers.SerializerMethodField()
    section4_url = serializers.SerializerMethodField()
    section5_url = serializers.SerializerMethodField()
    section6_url = serializers.SerializerMethodField()
    sectiondetails_url = serializers.SerializerMethodField()
    singlereview_url = serializers.SerializerMethodField()
    sectionreview_url = serializers.SerializerMethodField()
    # sectionimageslider1_url = serializers.SerializerMethodField()
    # sectionimageslider2_url = serializers.SerializerMethodField()




    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepage')
        return None

    def get_section1_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepagesectionone',args=[Homepage.slug])
        return None

    def get_section2_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepagesectiontwo',args=[Homepage.slug])
        return None


    # def get_sectionimageslider1_url(self, Homepage):
    #     if Homepage.slug:
    #         return reverse('HomepageSlidersection1',args=[Homepage.slug])
    #     return None

    # def get_sectionimageslider2_url(self, Homepage):
    #     if Homepage.slug:
    #         return reverse('HomepageSlidersection2',args=[Homepage.slug])
    #     return None


    def get_section3_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepagesectionthree',args=[Homepage.slug])
        return None

    def get_section4_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepagesectionfour',args=[Homepage.slug])
        return None

    def get_section5_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepagesectionfive',args=[Homepage.slug])
        return None

    def get_section6_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepagesectionsix',args=[Homepage.slug])
        return None

    def get_sectiondetails_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepagedetailsection',args=[Homepage.slug])
        return None

    def get_singlereview_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepagesinglereview',args=[Homepage.slug])
        return None

    def get_sectionreview_url(self, Homepage):
        if Homepage.slug:
            return reverse('homepagereviewsection',args=[Homepage.slug])
        return None



    class Meta:
        model = Homepage  
        fields = '__all__'






class PageDashboardSerializer(serializers.ModelSerializer):

    # sectiononeservices = ServicessectiononeSerializer(many=True, read_only=True)
    # sectiontwoservices = ServicessectiontwoSerializer(many=True, read_only=True)
    # sectionthreeservices = ServicessectionThreeSerializer(many=True, read_only=True)
    # servicesreviewpage = ServicesreviewSerializer(many=True, read_only=True)
    # servicesfaq = FaqSerializer(many=True, read_only=True)
    # sectionsixservices = ServicessectionsixSerializer(many=True, read_only=True)
    # sectionsevenservices = ServicessectionsevenSerializer(many=True, read_only=True)
    # slidersection = SlidersectionSerializer(many=True, read_only=True)



    section1_url = serializers.SerializerMethodField()
    section2_url = serializers.SerializerMethodField()
    section3_url = serializers.SerializerMethodField()
    section4_url = serializers.SerializerMethodField()
    section5_url = serializers.SerializerMethodField()
    section6_url = serializers.SerializerMethodField()
    section7_url = serializers.SerializerMethodField()
    section8_url = serializers.SerializerMethodField()
    blogsection_url = serializers.SerializerMethodField()
    ourwork_url = serializers.SerializerMethodField()
    pagethumbnail_path = serializers.SerializerMethodField()
    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Page):
        if Page.slug:
            return reverse('servicespages',args=[Page.slug])
        return None

    def get_section1_url(self, Page):
        if Page.slug:
            return reverse('servicessectionone',args=[Page.slug])
        return None

    def get_section2_url(self, Page):
        if Page.slug:
            return reverse('servicessectiontwo',args=[Page.slug])
        return None

    def get_section3_url(self, Page):
        if Page.slug:
            return reverse('servicessectionthree',args=[Page.slug])
        return None

    def get_section4_url(self, Page):
        if Page.slug:
            return reverse('servicessectionreviews',args=[Page.slug])
        return None

    def get_section5_url(self, Page):
        if Page.slug:
            return reverse('servicessectionfaq',args=[Page.slug])
        return None

    def get_section6_url(self, Page):
        if Page.slug:
            return reverse('servicessectionsix',args=[Page.slug])
        return None

    def get_section7_url(self, Page):
        if Page.slug:
            return reverse('servicessectionseven',args=[Page.slug])
        return None

    def get_section8_url(self, Page):
        if Page.slug:
            return reverse('sliderimage',args=[Page.slug])
        return None

    def get_blogsection_url(self, Page):
        if Page.slug:
            return reverse('servicesBlogPost',args=[Page.slug])
        return None

    def get_ourwork_url(self, Page):
        if Page.slug:
            return reverse('servicesourwork',args=[Page.slug])
        return None

    def get_pagethumbnail_path(self, Page):
        if Page.pageimg:
            return Page.pageimg.image.url
        return None

    class Meta:
        model = Page
        exclude = ['whyus', 'ourwork','blog','pricing','homepage',]

    def create(self, validated_data):
        # Get or create the first objects from Homepage, Pricing, and Whyus models
        homepage, homePage = Homepage.objects.get_or_create()
        pricing, pricepage = Pricing.objects.get_or_create()
        whyus, whyuspage = Whyus.objects.get_or_create()
        ourwork, ourworkpage = Ourwork.objects.get_or_create()
        blog, blogpage = Blogs.objects.get_or_create()
        
        if homepage:
            homepage.title = "homePage"
            homepage.save()
        if pricepage:
            pricing.title = "pricepage"
            pricing.save()
        if whyuspage:
            whyus.title = "whyuspage"
            whyus.save()
        if ourworkpage: 
            ourwork.title = "ourworkpage"
            ourwork.save()
        if blogpage:
            blog.title = "blogpage"
            blog.save()

        # Assign the related objects to the Page model
        validated_data['whyus'] = whyus
        validated_data['ourwork'] = ourwork
        validated_data['blog'] = blog
        validated_data['pricing'] = pricing
        validated_data['homepage'] = homepage

        return super().create(validated_data)









class OurworkSerializer(serializers.ModelSerializer):

    # sectiononeourwork = ServicessectiononeSerializer(many=True, read_only=True)
    # sectiontwoourwork = ServicessectiontwoSerializer(many=True, read_only=True)




    section1_url = serializers.SerializerMethodField()
    section2_url = serializers.SerializerMethodField()


    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Ourwork):
        if Ourwork.slug:
            return reverse('ourwork')
        return None

    def get_section1_url(self, Ourwork):
        if Ourwork.slug:
            return reverse('ourworksectionone',args=[Ourwork.slug])
        return None

    def get_section2_url(self, Ourwork):
        if Ourwork.slug:
            return reverse('ourworksectiontwo',args=[Ourwork.slug])
        return None



    class Meta:
        model = Ourwork  
        fields = '__all__'


class OurworksectiononeSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    def get_video_url(self, Ourworksectionone):
          if Ourworksectionone.sectiontwovideo:
             return obj.sectiontwovideo.video.url
          return None


    def get_photo_url(self, Ourworksectionone):
        if Ourworksectionone.sectiononeimg:
            return Ourworksectionone.sectiononeimg.image.url
        return None

    class Meta:
        model = Ourworksectionone
        fields = '__all__'


class OurworksectiontwoSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, Ourworksectiontwo):
        if Ourworksectiontwo.sectiontwoimg:
            return Ourworksectiontwo.sectiontwoimg.image.url
        return None

    class Meta:
        model = Ourworksectiontwo
        fields = '__all__'

class PageourworkSerializer(serializers.ModelSerializer):

    # pagethumbnail_path = serializers.SerializerMethodField()
    ourworkpage_url = serializers.SerializerMethodField()

    def get_ourworkpage_url(self, Page):
        if Page.slug:
            return reverse('ourworkresult',args=[Page.slug])
        return None


    # def get_pagethumbnail_path(self, Page):
    #     if Page.pageimg:
    #         return Page.pageimg.image.url
    #     return None

    class Meta:
        model = Page  
        fields = ['title','pageimg','discription','ourworkpage_url']

class OurworkUserSerializer(serializers.ModelSerializer):

    ourworksectionone = OurworksectiononeSerializer(many=True, read_only=True)
    ourworksectiontwo = OurworksectiontwoSerializer(many=True, read_only=True)
    Ourworkservicepages = PageourworkSerializer(many=True, read_only=True)



    class Meta:
        model = Ourwork
        fields = '__all__'


class BlogsSerializer(serializers.ModelSerializer):

    # sectiononeourwork = ServicessectiononeSerializer(many=True, read_only=True)
    # sectiontwoourwork = ServicessectiontwoSerializer(many=True, read_only=True)




    section1_url = serializers.SerializerMethodField()
    section2_url = serializers.SerializerMethodField()
    section3_url = serializers.SerializerMethodField()
    section4_url = serializers.SerializerMethodField()
    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Blogs):
        if Blogs.slug:
            return reverse('blogs')
        return None

    def get_section1_url(self, Blogs):
        if Blogs.slug:
            return reverse('blogsectionone',args=[Blogs.slug])
        return None

    def get_section2_url(self, Blogs):
        if Blogs.slug:
            return reverse('blogsectiontwo',args=[Blogs.slug])
        return None

    def get_section3_url(self, Blogs):
        if Blogs.slug:
            return reverse('blogsectionthree',args=[Blogs.slug])
        return None

    def get_section4_url(self, Blogs):
        if Blogs.slug:
            return reverse('blogsectionfour',args=[Blogs.slug])
        return None



    class Meta:
        model = Blogs  
        fields = '__all__'




class BlogsectiononeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogsectionone
        fields = '__all__'

class BlogsectiontwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogsectiontwo
        fields = '__all__'

class BlogsectionthreeSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, Blogsectionthree):
        if Blogsectionthree.sectionthreeimg:
            return Blogsectionthree.sectionthreeimg.image.url
        return None

    class Meta:
        model = Blogsectionthree
        fields = '__all__'

class BlogsectionfourSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, Blogsectionfour):
        if Blogsectionfour.sectionfourimg:
            return Blogsectionfour.sectionfourimg.image.url
        return None

    class Meta:
        model = Blogsectionfour
        fields = '__all__'


class blogsingleSerializer(serializers.ModelSerializer):
    page_url = serializers.SerializerMethodField()
    blogthumbnailimg_path = serializers.SerializerMethodField()
    Postauthor = BlogauthorSerializer(read_only=True)
    tag = TagSerializer(many=True,read_only=True)



    def get_blogthumbnailimg_path(self, BlogPost):
        if BlogPost.thumbnail:
            return BlogPost.thumbnail.image.url
        return None

    def get_page_url(self, BlogPost):
        if BlogPost.slug:
            return reverse('singleblog',args=[BlogPost.slug])
        return None

    class Meta:
        model = BlogPost
        fields = '__all__'

# class bloghomesingleSerializer(serializers.ModelSerializer):
#     page_url = serializers.SerializerMethodField()
#     blogthumbnailimg_path = serializers.SerializerMethodField()
#     Postauthor = BlogauthorSerializer(read_only=True)
#     tag = TagSerializer(many=True,read_only=True)



#     def get_blogthumbnailimg_path(self, BlogPost):
#         if BlogPost.thumbnail:
#             return BlogPost.thumbnail.image.url
#         return None

#     def get_page_url(self, BlogPost):
#         if BlogPost.slug:
#             return reverse('singleblog',args=[BlogPost.slug])
#         return None

#     class Meta:
#         model = BlogPost
#         fields = '__all__'

class PageblogSerializer(serializers.ModelSerializer):

    servicesBlogPost = blogsingleSerializer(many=True, read_only=True)
    blogthumbnailimg_path = serializers.SerializerMethodField()


    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Page):
        if Page.slug:
            return reverse('blogbycategory',args=[Page.slug])
        return None

    def get_blogthumbnailimg_path(self, Page):
        if Page.pageimg:
            return Page.pageimg.image.url
        return None

    class Meta:
        model = Page
        fields = '__all__'   

###timepass

class PageHomeblogSerializer(serializers.ModelSerializer):

    # servicesBlogPost = blogsingleSerializer(many=True, read_only=True)
    blogthumbnailimg_path = serializers.SerializerMethodField()


    page_url = serializers.SerializerMethodField()
    blogs = serializers.SerializerMethodField()

    def get_blogs(self, obj):
        blog_posts = BlogPost.objects.filter(page=obj)[:3]
        serializer = blogsingleSerializer(blog_posts, many=True)
        return serializer.data

    def get_page_url(self, Page):
        if Page.slug:
            return reverse('blogbycategory',args=[Page.slug])
        return None

    def get_blogthumbnailimg_path(self, Page):
        if Page.pageimg:
            return Page.pageimg.image.url
        return None

    class Meta:
        model = Page
        fields = '__all__'   

class BlogUserSerializer(serializers.ModelSerializer):

    blogsectionone = BlogsectiononeSerializer(many=True, read_only=True)
    Blogsservicepages = PageblogSerializer(many=True, read_only=True)
    blogsectiontwo = BlogsectiontwoSerializer(many=True, read_only=True)
    Blogsectionthree = BlogsectionthreeSerializer(many=True, read_only=True)
    Blogsectionfour = BlogsectionfourSerializer(many=True, read_only=True)


    class Meta:
        model = Blogs
        fields = '__all__'

##timepass

class BlogTimepassUserSerializer(serializers.ModelSerializer):

    blogsectionone = BlogsectiononeSerializer(many=True, read_only=True)
    Blogsservicepages = PageHomeblogSerializer(many=True, read_only=True)
    blogsectiontwo = BlogsectiontwoSerializer(many=True, read_only=True)
    Blogsectionthree = BlogsectionthreeSerializer(many=True, read_only=True)
    Blogsectionfour = BlogsectionfourSerializer(many=True, read_only=True)


    class Meta:
        model = Blogs
        fields = '__all__'



class WhyusSerializer(serializers.ModelSerializer):

    # sectiononeourwork = ServicessectiononeSerializer(many=True, read_only=True)
    # sectiontwoourwork = ServicessectiontwoSerializer(many=True, read_only=True)

    section1_url = serializers.SerializerMethodField()
    section2_url = serializers.SerializerMethodField()
    section3_url = serializers.SerializerMethodField()
    section4_url = serializers.SerializerMethodField()
    section5_url = serializers.SerializerMethodField()
    section6_url = serializers.SerializerMethodField()
    # section7_url = serializers.SerializerMethodField()
    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Whyus):
        if Whyus.slug:
            return reverse('whyus')
        return None

    def get_section1_url(self, Whyus):
        if Whyus.slug:
            return reverse('whyussectionone',args=[Whyus.slug])
        return None

    def get_section2_url(self, Whyus):
        if Whyus.slug:
            return reverse('whyussectiontwo',args=[Whyus.slug])
        return None

    def get_section3_url(self, Whyus):
        if Whyus.slug:
            return reverse('whyussectionthree',args=[Whyus.slug])
        return None

    def get_section4_url(self, Whyus):
        if Whyus.slug:
            return reverse('whyussectionfour',args=[Whyus.slug])
        return None

    def get_section5_url(self, Whyus):
        if Whyus.slug:
            return reverse('whyussectionfive',args=[Whyus.slug])
        return None

    def get_section6_url(self, Whyus):
        if Whyus.slug:
            return reverse('whyussectionsix',args=[Whyus.slug])
        return None

    # def get_section7_url(self, Whyus):
    #     if Whyus.slug:
    #         return reverse('whyusreview',args=[Whyus.slug])
    #     return None



    class Meta:
        model = Whyus  
        fields = '__all__'



class WhyussectionsevenSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    # video_url = serializers.SerializerMethodField()

    # def get_video_url(self, Ourworksectionone):
    #       if Ourworksectionone.sectiontwovideo:
    #          return obj.sectiontwovideo.video.url
    #       return None


    def get_photo_url(self, Whyussectionseven):
        if Whyussectionseven.sectionsevenimg:
            return Whyussectionseven.sectionsevenimg.image.url
        return None

    class Meta:
        model = Whyussectionseven
        fields = '__all__'


class WhyussectionsixSerializer(serializers.ModelSerializer):
    sectiononeimage1_path = serializers.SerializerMethodField()
    sectiononeimage2_path = serializers.SerializerMethodField()
    sectiononeimage3_path = serializers.SerializerMethodField()
    sectiononeimage4_path = serializers.SerializerMethodField()
    sectiononeimage5_path = serializers.SerializerMethodField()
    sectiononeimage6_path = serializers.SerializerMethodField()



    def get_sectiononeimage1_path(self, obj):
        if obj.sectionsiximage1:
            return obj.sectionsiximage1.image.url
        return None

    def get_sectiononeimage2_path(self, obj):
        if obj.sectionsiximage2:
            return obj.sectionsiximage2.image.url
        return None

    def get_sectiononeimage3_path(self, obj):
        if obj.sectionsiximage3:
            return obj.sectionsiximage3.image.url
        return None

    def get_sectiononeimage4_path(self, obj):
        if obj.sectionsiximage4:
            return obj.sectionsiximage4.image.url
        return None

    def get_sectiononeimage5_path(self, obj):
        if obj.sectionsiximage5:
            return obj.sectionsiximage5.image.url
        return None
    
    def get_sectiononeimage6_path(self, obj):
        if obj.sectionsiximage6:
            return obj.sectionsiximage6.image.url
        return None

    class Meta:
        model = Whyussectionsix
        fields = '__all__'


class WhyussectionfiveSerializer(serializers.ModelSerializer):
    sectiononeimage1_path = serializers.SerializerMethodField()
    sectiononeimage2_path = serializers.SerializerMethodField()
    sectiononeimage3_path = serializers.SerializerMethodField()


    def get_sectiononeimage1_path(self, obj):
        if obj.sectionfiveimage1:
            return obj.sectionfiveimage1.image.url
        return None

    def get_sectiononeimage2_path(self, obj):
        if obj.sectionfiveimage2:
            return obj.sectionfiveimage2.image.url
        return None

    def get_sectiononeimage3_path(self, obj):
        if obj.sectionfiveimage3:
            return obj.sectionfiveimage3.image.url
        return None

    class Meta:
        model = Whyussectionfive
        fields = '__all__'



class WhyussectionfourSerializer(serializers.ModelSerializer):


    class Meta:
        model = Whyussectionfour
        fields = '__all__'


class WhyussectionthreeSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    def get_video_url(self, Whyussectionthree):
          if Whyussectionthree.sectionthreevideo:
             return Whyussectionthree.sectionthreevideo.video.url
          return None


    def get_photo_url(self, Whyussectionthree):
        if Whyussectionthree.sectionthreevideoimg:
            return Whyussectionthree.sectionthreevideoimg.image.url
        return None

    class Meta:
        model = Whyussectionthree
        fields = '__all__'




class WhyussectiontwoSerializer(serializers.ModelSerializer):
    photo1_url = serializers.SerializerMethodField()
    photo2_url = serializers.SerializerMethodField()

    def get_photo1_url(self, Whyussectiontwo):
          if Whyussectiontwo.sectiontwoimage1:
             return Whyussectiontwo.sectiontwoimage1.image.url
          return None


    def get_photo2_url(self, Whyussectiontwo):
        if Whyussectiontwo.sectiontwoimage2:
            return Whyussectiontwo.sectiontwoimage2.image.url
        return None

    class Meta:
        model = Whyussectiontwo
        fields = '__all__'



# class whyusreviewSerializer(serializers.ModelSerializer):


#     class Meta:
#         model = whyusreview
#         fields = '__all__'


class WhyusUserSerializer(serializers.ModelSerializer):

    whyussectionseven = WhyussectionsevenSerializer(many=True, read_only=True)
    Whyussectiontwo = WhyussectiontwoSerializer(many=True, read_only=True)
    Whyussectionthree = WhyussectionthreeSerializer(many=True, read_only=True)
    Whyussectionfour = WhyussectionfourSerializer(many=True, read_only=True)
    Whyussectionfive = WhyussectionfiveSerializer(many=True, read_only=True)
    Whyussectionsix = WhyussectionsixSerializer(many=True, read_only=True)
    # whyusreview = whyusreviewSerializer(many=True, read_only=True)
    # Whyussectionthree = WhyussectionthreeSerializer(many=True, read_only=True)
    # Whyussectiontwo = WhyussectiontwoSerializer(many=True, read_only=True)
    # Whyussectionthree = WhyussectionthreeSerializer(many=True, read_only=True)


    class Meta:
        model = Whyus  
        fields = '__all__'


# class PricinguserreviewSerializer(serializers.ModelSerializer):


#     class Meta:
#         model = Pricinguserreview
#         fields = '__all__'


class PricingFaqSerializer(serializers.ModelSerializer):


    class Meta:
        model = PricingFaq
        fields = '__all__'

class PricingsectiononeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Pricingsectionone
        fields = '__all__'

class PricingSerializer(serializers.ModelSerializer):

    section1_url = serializers.SerializerMethodField()
    section2_url = serializers.SerializerMethodField()
    section3_url = serializers.SerializerMethodField()
    section4_url = serializers.SerializerMethodField()
    section5_url = serializers.SerializerMethodField()
    # section6_url = serializers.SerializerMethodField()
    section7_url = serializers.SerializerMethodField()
    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Pricing):
        if Pricing.slug:
            return reverse('pricing')
        return None

    def get_section1_url(self, Pricing):
        if Pricing.slug:
            return reverse('Pricingsectionone',args=[Pricing.slug])
        return None

    def get_section2_url(self, Pricing):
        if Pricing.slug:
            return reverse('Pricingsectiontwo',args=[Pricing.slug])
        return None

    def get_section3_url(self, Pricing):
        if Pricing.slug:
            return reverse('Pricingsectionthree',args=[Pricing.slug])
        return None

    def get_section4_url(self, Pricing):
        if Pricing.slug:
            return reverse('Pricingsectionfour',args=[Pricing.slug])
        return None

    def get_section5_url(self, Pricing):
        if Pricing.slug:
            return reverse('Pricingdetails',args=[Pricing.slug])
        return None

    # def get_section6_url(self, Pricing):
    #     if Pricing.slug:
    #         return reverse('Pricinguserreview',args=[Pricing.slug])
    #     return None

    def get_section7_url(self, Pricing):
        if Whyus.slug:
            return reverse('PricingFaq',args=[Pricing.slug])
        return None


    class Meta:
        model = Pricing
        fields = '__all__'


class PricingsectiontwoSerializer(serializers.ModelSerializer):

    document_url = serializers.SerializerMethodField()

    def get_document_url(self, Pricingsectiontwo):
          if Pricingsectiontwo.pricepdf:
             return Pricingsectiontwo.pricepdf.url
          return None

    class Meta:
        model = Pricingsectiontwo
        fields = '__all__'

class PricingsectionthreeSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    def get_video_url(self, Pricingsectionthree):
          if Pricingsectionthree.sectionthreevideo:
             return Pricingsectionthree.sectionthreevideo.video.url
          return None


    def get_photo_url(self, Pricingsectionthree):
        if Pricingsectionthree.sectionthreevideoimg:
            return Pricingsectionthree.sectionthreevideoimg.image.url
        return None

    class Meta:
        model = Pricingsectionthree
        fields = '__all__'


class PricingsectionfourSerializer(serializers.ModelSerializer):
    sectiononeimage1_path = serializers.SerializerMethodField()
    sectiononeimage2_path = serializers.SerializerMethodField()
    sectiononeimage3_path = serializers.SerializerMethodField()
    sectiononeimage4_path = serializers.SerializerMethodField()
    sectiononeimage5_path = serializers.SerializerMethodField()
    sectiononeimage6_path = serializers.SerializerMethodField()



    def get_sectiononeimage1_path(self, obj):
        if obj.sectionfourimage1:
            return obj.sectionfourimage1.image.url
        return None

    def get_sectiononeimage2_path(self, obj):
        if obj.sectionfourimage2:
            return obj.sectionfourimage2.image.url
        return None

    def get_sectiononeimage3_path(self, obj):
        if obj.sectionfourimage3:
            return obj.sectionfourimage3.image.url
        return None

    def get_sectiononeimage4_path(self, obj):
        if obj.sectionfourimage4:
            return obj.sectionfourimage4.image.url
        return None

    def get_sectiononeimage5_path(self, obj):
        if obj.sectionfourimage5:
            return obj.sectionfourimage5.image.url
        return None
    
    def get_sectiononeimage6_path(self, obj):
        if obj.sectionfourimage6:
            return obj.sectionfourimage6.image.url
        return None

    class Meta:
        model = Pricingsectionfour
        fields = '__all__'

class PricingsubdetailsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Pricingsubdetails
        fields = '__all__'

class PricingdetailsSerializer(serializers.ModelSerializer):

    pricingpage = PricingsubdetailsSerializer(many=True, read_only=True)


    class Meta:
        model = Pricingdetails
        fields = '__all__'

# class BlogauthorSerializer(serializers.ModelSerializer):
#     blogauthordp_path = serializers.SerializerMethodField()
#     authorblog_path = serializers.SerializerMethodField()


#     def get_blogauthordp_path(self, obj):
#         if obj.profilephoto:
#             return obj.profilephoto.image.url
#         return None

#     def get_authorblog_path(self, obj):
#         if obj.slug:
#             return reverse('authorname',args=[obj.slug])
#         return None

#     class Meta:
#         model = Blogauthor
#         fields = '__all__'


# class TagSerializer(serializers.ModelSerializer):


#     class Meta:
#         model = Tag
#         fields = '__all__'

# class PageSerializer(serializers.ModelSerializer):

#     pagethumbnail_path = serializers.SerializerMethodField()
#     page_url = serializers.SerializerMethodField()

#     def get_page_url(self, Page):
#         if Page.slug:
#             return reverse('servicespages',args=[Page.slug])
#         return None


#     def get_pagethumbnail_path(self, Page):
#         if Page.pageimg:
#             return Page.pageimg.image.url
#         return None

#     class Meta:
#         model = Page  
#         fields = ['title','pageimg','discription','pagethumbnail_path','page_url','slug',]


class PricingUserSerializer(serializers.ModelSerializer):

    Pricingsectionone = PricingsectiononeSerializer(many=True, read_only=True)
    Pricingdetails = PricingdetailsSerializer(many=True, read_only=True)
    Pricingsectiontwo = PricingsectiontwoSerializer(many=True,read_only=True)
    Pricingsectionthree = PricingsectionthreeSerializer(many=True, read_only=True)
    Pricingsectionfour = PricingsectionfourSerializer(many=True, read_only=True)
    # Pricinguserreview = PricinguserreviewSerializer(many=True, read_only=True)
    PricingFaq = PricingFaqSerializer(many=True, read_only=True)
    Pricingservicepages = PageSerializer(many=True, read_only=True)

    class Meta:
        model = Pricing
        fields = '__all__'


class WorkresultSerializer(serializers.ModelSerializer):

    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Ourworkproject):
        if Ourworkproject.slug:
            return reverse('ourworksingle', args=[Ourworkproject.page.slug, Ourworkproject.slug])
        return None
        
    class Meta:
        model = Ourworkproject
        fields = '__all__'



# class WorkresultSerializer(serializers.ModelSerializer):

#     # page_url = serializers.SerializerMethodField()

#     # def get_page_url(self, Ourworkproject):
#     #     if Ourworkproject.slug:
#     #         return reverse('ourworksingle', args=[self.page.slug, self.slug])
#     #     return None
        
#     class Meta:
#         model = Ourworkproject
#         fields = '__all__'

class ServicesuserSerializer(serializers.ModelSerializer):

    sectiononeservices = ServicessectiononeSerializer(many=True, read_only=True)
    sectiontwoservices = ServicessectiontwoSerializer(read_only=True,many=True)
    sectionthreeservices = ServicessectionThreeSerializer(many=True, read_only=True)
    # servicesreviewpage = ServicesreviewSerializer(many=True, read_only=True)
    servicesfaq = FaqSerializer(many=True, read_only=True)
    sectionsixservices = ServicessectionsixSerializer(many=True, read_only=True)
    sectionsevenservices = ServicessectionsevenSerializer(many=True, read_only=True)
    # slidersection = SlidersectionSerializer(many=True, read_only=True)

        
    class Meta:
        model = Page
        fields = '__all__'

######## Bookaserializer ####

class BookacallSerializer(serializers.ModelSerializer):



    section1_url = serializers.SerializerMethodField()
    section2_url = serializers.SerializerMethodField()
    section3_url = serializers.SerializerMethodField()
    section4_url = serializers.SerializerMethodField()
    page_url = serializers.SerializerMethodField()

    def get_page_url(self, Bookacall):
        if Bookacall.slug:
            return reverse('bookacalldashboard')
        return None

    def get_section1_url(self, Bookacall):
        if Bookacall.slug:
            return reverse('bookacallsection1',args=[Bookacall.slug])
        return None

    def get_section2_url(self, Bookacall):
        if Bookacall.slug:
            return reverse('bookacallsection2',args=[Bookacall.slug])
        return None

    def get_section3_url(self, Bookacall):
        if Bookacall.slug:
            return reverse('bookacallslider1section',args=[Bookacall.slug])
        return None

    def get_section4_url(self, Bookacall):
        if Bookacall.slug:
            return reverse('bookacallslider2section',args=[Bookacall.slug])
        return None




    class Meta:
        model = Bookacall  
        fields = '__all__'


class BookacallsectiononeSerializer(serializers.ModelSerializer):
    sectiononeimage1_path = serializers.SerializerMethodField()
    sectiononeimage2_path = serializers.SerializerMethodField()
    sectiononeimage3_path = serializers.SerializerMethodField()



    def get_sectiononeimage1_path(self, obj):
        if obj.sectiononeimg1:
            return obj.sectiononeimg1.image.url
        return None

    def get_sectiononeimage2_path(self, obj):
        if obj.sectiononeimg2:
            return obj.sectiononeimg2.image.url
        return None

    def get_sectiononeimage3_path(self, obj):
        if obj.sectiononeimg3:
            return obj.sectiononeimg3.image.url
        return None



    class Meta:
        model = Bookacallsectionone
        fields = '__all__'


class BookacallsectiontwoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Bookacallsectiontwo
        fields = '__all__'


# class BookacallSlidersection1Serializer(serializers.ModelSerializer):
#       sectiononeimage1_path = serializers.SerializerMethodField()


#       def get_sectiononeimage1_path(self, obj):
#          if obj.sliderimage:
#             return obj.sliderimage.image.url
#          return None

#       class Meta:
#             model = BookacallSlidersection1
#             fields = '__all__'

# class BookacallSlidersection2Serializer(serializers.ModelSerializer):
#       sectiononeimage1_path = serializers.SerializerMethodField()


#       def get_sectiononeimage1_path(self, obj):
#          if obj.sliderimage:
#             return obj.sliderimage.image.url
#          return None

#       class Meta:
#             model = BookacallSlidersection2
#             fields = '__all__'


class bookcallUserSerializer(serializers.ModelSerializer):

    Bookacallsectionone = BookacallsectiononeSerializer(many=True, read_only=True)
    Bookacallsectiontwo = BookacallsectiontwoSerializer(many=True, read_only=True)
    # BookacallSlidersection1 = BookacallSlidersection1Serializer(many=True, read_only=True)
    # BookacallSlidersection2 = BookacallSlidersection2Serializer(many=True, read_only=True)


    class Meta:
        model = Bookacall
        fields = '__all__'

class SocialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Social
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emailinput
        fields = '__all__'

# from rest_framework.pagination import PageNumberPagination
# from rest_framework.views import Request

# class BlogPostPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class blogpageauthorSerializer(serializers.ModelSerializer):

    blogpostauthor = blogsingleSerializer(read_only=True,many=True)
    blogauthordp_path = serializers.SerializerMethodField()
    authorblog_path = serializers.SerializerMethodField()
    # blogpostauthor = serializers.SerializerMethodField()



    def get_blogauthordp_path(self, obj):
        if obj.profilephoto:
            return obj.profilephoto.image.url
        return None

    def get_authorblog_path(self, obj):
        if obj.slug:
            return reverse('authorname',args=[obj.slug])
        return None

    # def get_blogpostauthor(self, obj):
    #     request = self.context.get('request')
    #     page_size = Request(request).query_params.get('page_size')
    #     paginator = BlogPostPagination()
    #     blog_posts = obj.blogpostauthor.all()
    #     result_page = paginator.paginate_queryset(blog_posts, request)
    #     serializer = BlogPostSerializer(result_page, many=True, context={'request': request})
    #     return {
    #         'results': serializer.data,
    #         'count': blog_posts.count(),
    #         'previous': paginator.get_previous_link(),
    #         'next': paginator.get_next_link(),
    #     }

    class Meta:
        model = Blogauthor
        fields = '__all__'


class authordetailsSerializer(serializers.ModelSerializer):
    blogauthordp_path = serializers.SerializerMethodField()
    # authorblog_path = serializers.SerializerMethodField()


    def get_blogauthordp_path(self, obj):
        if obj.profilephoto:
            return obj.profilephoto.image.url
        return None

    # def get_authorblog_path(self, obj):
    #     if obj.slug:
    #         return reverse('authorname',args=[obj.slug])
    #     return None

    class Meta:
        model = Blogauthor
        fields = '__all__'
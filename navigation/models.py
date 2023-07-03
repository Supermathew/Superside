from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
import re
from ckeditor_uploader.fields import RichTextUploadingField




# Create your models here.


class MediaBucket(models.Model):
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f'files' 

class Menu(models.Model):
      url = models.CharField(max_length=200,null=True,blank=True)
      name = models.CharField(max_length=200)
      menu_isbtn = models.BooleanField(default=False)




      def __(self):
        return self.name

class SubMenu(models.Model):
      menu = models.ForeignKey(Menu, on_delete=models.CASCADE,null=True,blank=True,related_name='sub_menu')
      name = models.CharField(max_length=100)
      url = models.CharField(max_length=200)

      def __(self):
        return self.id



class Header(models.Model):
      headerlogo = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='logo')
      menu = models.ForeignKey(Menu, on_delete=models.CASCADE,null=True,blank=True,related_name='header')

      def __str__(self):
         return str(self.id)

class Footer(models.Model):
      Footerheading = models.TextField(null=True,blank=True)
      footerdiscrip = models.TextField(null=True,blank=True)
      footeremailpageholder = models.TextField(null=True,blank=True)
      footersubscription = models.TextField(null=True,blank=True)
      footersmalldisbold = models.TextField(null=True,blank=True)
      footersmalldis = models.TextField(null=True,blank=True)
      footercopyrighttext = models.TextField(null=True,blank=True)
      footerprivacy = models.TextField(null=True,blank=True)
      footerprivacylink = models.TextField(null=True,blank=True)
      footerterms = models.TextField(null=True,blank=True)
      footertermsofuselink = models.TextField(null=True,blank=True)
      footerstatuspage = models.TextField(null=True,blank=True)
      footerstatuspagelink = models.TextField(null=True,blank=True)
      text14 = models.TextField(null=True,blank=True)
      text15 = models.TextField(null=True,blank=True)

      def __str__(self):
         return f'Footer' 

class Homepage(models.Model):

      # def remove_numbers(value):
      #     return re.sub(r'\d', '', value)

      title = models.TextField(null=True,blank=True,unique=True)
      slug = AutoSlugField(populate_from='title', unique=True)


      def __str__(self):
          return self.title

      def save(self, *args, **kwargs):
            if self.title != self.slug:  # Only update the slug if the title has changed
                  self.slug = slugify(self.title)
            super().save(*args, **kwargs)

class Sectiontwo(models.Model):
      text1 = models.TextField(null=True,blank=True)
      text2 = models.TextField(null=True,blank=True)
      text3 = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagesectiontwo')

      def __str__(self):
         return f'Sectiontwo'

class Facts(models.Model):
      subTitle1 = models.TextField(null=True,blank=True)
      title1 = models.TextField(null=True,blank=True)
      desc1 = models.TextField(null=True,blank=True)
      subTitle2 = models.TextField(null=True,blank=True)
      title2 = models.TextField(null=True,blank=True)
      desc2 = models.TextField(null=True,blank=True)
      subTitle3 = models.TextField(null=True,blank=True)
      title3 = models.TextField(null=True,blank=True)
      desc3 = models.TextField(null=True,blank=True)
      subTitle4 = models.TextField(null=True,blank=True)
      title4 = models.TextField(null=True,blank=True)
      desc4 = models.TextField(null=True,blank=True)

      def __str__(self):
         return f'Facts'


class Sectionfour(models.Model):
      sectionfourtitle = models.TextField(null=True,blank=True)
      Sectionfourdiscription = models.TextField(null=True,blank=True)
      Sectionfourbtntext = models.TextField(null=True,blank=True)
      Sectionfourbtnurl = models.TextField(null=True,blank=True)
      sectionfoursubdiscription = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='HomepageSectionfour')


      def __str__(self):
         return f'Sectionfour'

class Sectionfive(models.Model):
      sectionfiveheading = models.TextField(null=True,blank=True)
      sectionfivesubheading = models.TextField(null=True,blank=True)
      sectionfiveimage1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagesectionfiveimage1')
      sectionfiveimage1details = models.TextField(null=True,blank=True)
      sectionfiveimage2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagesectionfiveimage2')
      sectionfiveimage2details = models.TextField(null=True,blank=True)
      sectionfiveimage3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagesectionfiveimage3')
      sectionfiveimage3details = models.TextField(null=True,blank=True)
      sectionfiveimage4 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagesectionfiveimage4')
      sectionfiveimage4details = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='HomepageSectionfive')

      def __str__(self):
         return f'Sectionfive'

class Singlereview(models.Model):
      Singlereviewtext = models.TextField(null=True,blank=True)

      def __str__(self):
         return f'singlereview'


class Sectionsix(models.Model):
      sectionsixsubtitle = models.TextField(null=True,blank=True)
      sectionsixtitle = models.TextField(null=True,blank=True)
      sectionsixdisc = models.TextField(null=True,blank=True)
      sectionsixbtntext = models.TextField(null=True,blank=True)
      sectionsixbtnurl = models.TextField(null=True,blank=True)
      sectionsixbgurl = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagesectionsiximage1')
      sectionsixmobileimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagesectionsiximage2')
      page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='HomepageSectionsix')


      def __str__(self):
         return f'Sectionsix'
  
class Sectionone(models.Model):
      sectiononeheading = models.TextField(null=True,blank=True)
      sectiononesubheading = models.TextField(null=True,blank=True)
      sectiononeemailinput = models.TextField(null=True,blank=True)
      sectiononegetstartedbtn = models.TextField(null=True,blank=True)
      sectiononebtnurl = models.TextField(null=True,blank=True)
      sectiononedisplaytext = models.TextField(null=True,blank=True)
      sectiononeimage1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiononeimage1')
      sectiononeimage2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiononeimage2')
      sectiononeimage3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiononeimage3')
      sectiononeimage4 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiononeimage4')
      sectiononeimage5 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiononeimage5')
      page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagesectionone')

      def __str__(self):
         return f'Sectionone'




class VideoBucket(models.Model):
    video = models.FileField(upload_to='video/')

    def __str__(self):
        return self.id 


class Sectionthree(models.Model):
      sectionthreeheading = models.TextField(null=True,blank=True)
      sectionthreesubheading = models.TextField(null=True,blank=True)
      sectionthreediscription = models.TextField(null=True,blank=True)
      sectionthreebtntext = models.TextField(null=True,blank=True)
      sectionthreebtnurl = models.TextField(null=True,blank=True)
      sectionthreevideodiscription = models.TextField(null=True,blank=True)
      sectionthreeheading1 = models.TextField(null=True,blank=True)
      sectionthreesubheading1 = models.TextField(null=True,blank=True)
      sectionthreediscription1 = models.TextField(null=True,blank=True)
      sectionthreegetstartedbtn = models.TextField(null=True,blank=True)
      sectionthreebtnurl = models.TextField(null=True,blank=True)
      sectionthreevideo = models.ForeignKey(VideoBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionthreevideo')
      page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagesectionthree')

      def __str__(self):
         return f'Sectionthree'



class Details(models.Model):
      detailsheading = models.TextField(null=True,blank=True)
      detailsdiscription = models.TextField(null=True,blank=True)
      detailsimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='detailsimage')
      page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagedetails')

      def __str__(self):
         return f'Details'


class CommonReview(models.Model):
      username = models.TextField()
      userdesignation = models.TextField()
      userreview = models.TextField()
      userphoto = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='userphoto')
      # page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='Homepagereview')

      def __str__(self):
         return f'Homepagereview'

class CommonSlidersection1(models.Model):
      sliderimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='homepagesliderimagesection1')
      # page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='HomepageSlidersection1')

      def __str__(self):
         return f'HomepageSlidersection1'


class CommonSlidersection2(models.Model):
      sliderimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='homepagesliderimagesection2')
      # page = models.ForeignKey(Homepage, on_delete=models.CASCADE,null=True,blank=True,related_name='HomepageSlidersection2')

      def __str__(self):
         return f'HomepageSlidersection2'



class Whyus(models.Model):

      # def remove_numbers(value):
      #     return re.sub(r'\d', '', value)


      title = models.TextField(null=True,blank=True,unique=True)
      slug = AutoSlugField(populate_from='title', unique=True)




      def __str__(self):
          return self.title

      def save(self, *args, **kwargs):
            if self.title != self.slug:  # Only update the slug if the title has changed
                  self.slug = slugify(self.title)
            super().save(*args, **kwargs)

class Ourwork(models.Model):

      # def remove_numbers(value):
      #     return re.sub(r'\d', '', value)


      title = models.TextField(null=True,blank=True,unique=True)
      slug = AutoSlugField(populate_from='title', unique=True)




      def __str__(self):
          return self.title

      def save(self, *args, **kwargs):
            if self.title != self.slug:  # Only update the slug if the title has changed
                  self.slug = slugify(self.title)
            super().save(*args, **kwargs)
      
class Blogs(models.Model):

      # def remove_numbers(value):
      #     return re.sub(r'\d', '', value)


      title = models.TextField(null=True,blank=True,unique=True)
      slug = AutoSlugField(populate_from='title', unique=True)




      def __str__(self):
          return self.title

      def save(self, *args, **kwargs):
            if self.title != self.slug:  # Only update the slug if the title has changed
                  self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class Pricing(models.Model):

      #     def remove_numbers(value):
      #         return re.sub(r'\d', '', value)

      title = models.TextField(null=True, blank=True, unique=True)
      slug = AutoSlugField(populate_from='title', unique=True)

      def __str__(self):
            return self.title

      def save(self, *args, **kwargs):
            if self.title != self.slug:  # Only update the slug if the title has changed
                  self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class Page(models.Model):
#     @staticmethod
#     def remove_numbers(value):
#         return re.sub(r'\d', '', value)

    title = models.TextField(unique=True)
    discription = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True)
    whyus = models.ForeignKey(Whyus, on_delete=models.CASCADE, null=True,blank=True,related_name='whyusservicepages')
    ourwork = models.ForeignKey(Ourwork, on_delete=models.CASCADE, null=True,blank=True,related_name='Ourworkservicepages')
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, null=True,blank=True,related_name='Blogsservicepages')
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, null=True,blank=True,related_name='Pricingservicepages')
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE, null=True,blank=True,related_name='Homepageservicepages')
    pageimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='pageimage')





    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title != self.slug:  # Only update the slug if the title has changed
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

 


class Servicessectionone(models.Model):
      sectiontoneheading = models.TextField(null=True,blank=True)
      sectiontonesubheading = models.TextField(null=True,blank=True)
      sectiontonediscription = models.TextField(null=True,blank=True)
      sectiontonebtntext = models.TextField(null=True,blank=True)
      sectiontonebtnurl = models.TextField(null=True,blank=True)
      sectiontonesimpletext = models.TextField(null=True,blank=True)
      sectiontoneheading1 = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiononeservices')
      sectiontoneimage1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiontoneimage1')
      sectiontoneimage2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiontoneimage2')
      sectiontoneimage3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiontoneimage3')

      def __str__(self):
         return f'Servicessectionone'


class Servicessectiontwo(models.Model):
      sectiontwoheading = models.TextField(null=True,blank=True)
      sectiontwocolourtext = models.TextField(null=True,blank=True)
      sectiontwodiscription = models.TextField(null=True,blank=True)
      sectiontwobtntext = models.TextField(null=True,blank=True)
      sectiontwobtnurl = models.TextField(null=True,blank=True)
      sectiontwosimpletext = models.TextField(null=True,blank=True)
      sectiontwoheading1 = models.TextField(null=True,blank=True)
      sectiontwoheadin2 = models.TextField(null=True,blank=True)
      sectiontwosubheading2 = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiontwoservices')
      sectiontwovideo = models.ForeignKey(VideoBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiontwovideo')
      sectiontwoimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiontwoimage')
      sectiontwocoverimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectiontwocoverimage')

      def __str__(self):
         return f'Servicessectiontwo'



class ServicessectionThree(models.Model):
      sectionthreeheading = models.TextField(null=True,blank=True)
      sectionthreesubheading = models.TextField(null=True,blank=True)
      sectionthreecolourtext = models.TextField(null=True,blank=True)
      sectionthreetextheading = models.TextField(null=True,blank=True)
      sectionthreetextdiscription = models.TextField(null=True,blank=True)
      sectionthreeimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='servicessectionthreeimage')
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionthreeservices')

class Servicessectionfour(models.Model):
      sectiontfourheading = models.TextField(null=True,blank=True)
      sectiontfourdesigntext = models.TextField(null=True,blank=True)
      sectiontfourfaq = models.TextField(null=True,blank=True)
      sectiontfourfaqtext = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionfourservices')


      def __str__(self):
         return f'Servicessectionfour'


class servicescapabilities(models.Model):
      servicestext = models.TextField(null=True,blank=True)
      servicessubheading = models.TextField(null=True,blank=True)
      servicesimg = models.ForeignKey(MediaBucket,null=True,blank=True, on_delete=models.CASCADE,related_name='servicesimg')
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='servicescapability')

      def __str__(self):
         return f'servicescapabilities'

class Faq(models.Model):
      question = models.TextField()
      answer = models.TextField()

      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='servicesfaq')

      def __str__(self):
         return f'Servicesfaq'


class Servicessectionsix(models.Model):
      sectionsixheading = models.TextField(null=True,blank=True)
      sectionsixcolourtext = models.TextField(null=True,blank=True)
      sectionsixsubheading = models.TextField(null=True,blank=True)
      sectionsixparagraph = models.TextField(null=True,blank=True)
      sectionsixsubparagraph = models.TextField(null=True,blank=True)
      sectionsixbtntext = models.TextField(null=True,blank=True)
      sectionsixbtnurl = models.TextField(null=True,blank=True)
      sectionsiximage1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionsiximage1')
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionsixservices')

      def __str__(self):
         return f'Servicessectionsix'

class Userdata(models.Model):
      name = models.TextField()
      lastname = models.TextField()
      email = models.TextField()
      comapanyname = models.TextField()
      reasontocontact = models.TextField()
      phonenumber = models.IntegerField()
      page = models.TextField(null=True,blank=True)

      def __str__(self):
         return f'Userdata'


class Servicessectionseven(models.Model):
      sectionsevenheading = models.TextField(null=True,blank=True)
      sectionsevensubheading = models.TextField(null=True,blank=True)
      sectionsevenparagraph = models.TextField(null=True,blank=True)
      sectionsevenpoint1 = models.TextField(null=True,blank=True)
      sectionsevenpoint2 = models.TextField(null=True,blank=True)
      sectionsevenpoint3 = models.TextField(null=True,blank=True)
      sectionsevenpoint4 = models.TextField(null=True,blank=True)
      sectionsevenimage1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionsevenimage1')
      sectionsevenimage2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionsevenimage2')
      sectionsevenimage3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionsevenimage3')
      sectionsevenimage4 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionsevenimage4')
      sectionsevenimage5 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionsevenimage5')
      sectionsevenimage6 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionsevenimage6')
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionsevenservices')

      def __str__(self):
         return f'Servicessectionseven'


class Servicescta(models.Model):
      Servicesctaheading = models.TextField(null=True,blank=True)
      Servicesctasubheading = models.TextField(null=True,blank=True)
      Servicesctabtntext = models.TextField(null=True,blank=True)
      Servicesctabtnurl = models.TextField(null=True,blank=True)
      Servicesctaimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Servicesctaimg')
      Servicesctamobileimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Servicesctaimage2')
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='Servicescta')

      def __str__(self):
          return f'Servicescta'


class Ourworksectionone(models.Model):
      sectiononeheading = models.TextField(null=True,blank=True)
      sectiononesubheading = models.TextField(null=True,blank=True)
      sectiononediscription = models.TextField(null=True,blank=True)
      sectiononetext = models.TextField(null=True,blank=True)
      sectiononeimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='ourworksectiononeimg')
      page = models.ForeignKey(Ourwork, on_delete=models.CASCADE,null=True,blank=True,related_name='ourworksectionone')
      sectiontwovideo = models.ForeignKey(VideoBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='ourworksectiontwovideo')

      def __str__(self):
          return f'ourworksectionone'


class Ourworksectiontwo(models.Model):
      sectiontwoheading = models.TextField(null=True,blank=True)
      sectiontwosubheading = models.TextField(null=True,blank=True)
      sectiontwodiscription = models.TextField(null=True,blank=True)
      sectiontwotext = models.TextField(null=True,blank=True)
      sectiontwobtntext = models.TextField(null=True,blank=True)
      sectiontwobtnurl = models.TextField(null=True,blank=True)
      sectiontwoimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='ourworksectiontwoimg')
      page = models.ForeignKey(Ourwork, on_delete=models.CASCADE,null=True,blank=True,related_name='ourworksectiontwo')

      def __str__(self):
          return f'Ourworksectiontwo'




class Blogsectionone(models.Model):
      sectiononeheading = models.TextField(null=True,blank=True)
      sectiononesubheading = models.TextField(null=True,blank=True)
      sectiononediscription = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Blogs, on_delete=models.CASCADE,null=True,blank=True,related_name='blogsectionone')

      def __str__(self):
          return f'Blogsectionone'


class Blogsectiontwo(models.Model):
      sectiontwoheading = models.TextField(null=True,blank=True)
      sectiontwosubheading = models.TextField(null=True,blank=True)
      sectiontwodiscription = models.TextField(null=True,blank=True)
      sectiontwotext = models.TextField(null=True,blank=True)
      sectiontwobtntext = models.TextField(null=True,blank=True)
      sectiontwobtnurl = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Blogs, on_delete=models.CASCADE,null=True,blank=True,related_name='blogsectiontwo')

      def __str__(self):
          return f'Blogsectiontwo'  


class Blogsectionthree(models.Model):
      sectionthreeheading = models.TextField(null=True,blank=True)
      sectionthreesubheading = models.TextField(null=True,blank=True)
      sectionthreediscription = models.TextField(null=True,blank=True)
      sectionthreetext = models.TextField(null=True,blank=True)
      sectionthreebtntext = models.TextField(null=True,blank=True)
      sectionthreebtnurl = models.TextField(null=True,blank=True)
      sectionthreeimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='blogsectionthreeimg')
      page = models.ForeignKey(Blogs, on_delete=models.CASCADE,null=True,blank=True,related_name='Blogsectionthree')

      def __str__(self):
          return f'Blogsectionthree' 

class Blogsectionfour(models.Model):
      sectionfourheading = models.TextField(null=True,blank=True)
      sectionfoursubheading = models.TextField(null=True,blank=True)
      sectionfourdiscription = models.TextField(null=True,blank=True)
      sectionfourtext = models.TextField(null=True,blank=True)
      sectionfourbtnurl = models.TextField(null=True,blank=True)
      sectionfourimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='blogsectionfourimg')
      page = models.ForeignKey(Blogs, on_delete=models.CASCADE,null=True,blank=True,related_name='Blogsectionfour')

      def __str__(self):
          return f'Blogsectionfour'    





class Whyussectionseven(models.Model):
      sectionsevenheading = models.TextField(null=True,blank=True)
      sectionsevensubheading = models.TextField(null=True,blank=True)
      sectionsevenbtntext = models.TextField(null=True,blank=True)
      sectionsevenbtnurl = models.TextField(null=True,blank=True)
      sectionsevenimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionsevenimg')
      sectionsevenmobileimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionsevenimagemobileimg')
      page = models.ForeignKey(Whyus, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionseven')

      def __str__(self):
          return f'Whyussectionseven'

class Whyussectionsix(models.Model):
      sectionsixheading = models.TextField(null=True,blank=True)
      sectionsixsubheading = models.TextField(null=True,blank=True)
      sectionsixbtntext = models.TextField(null=True,blank=True)
      sectionsixbtnurl = models.TextField(null=True,blank=True)
      sectionsiximage1details = models.TextField(null=True,blank=True)
      sectionsiximage2details = models.TextField(null=True,blank=True)
      sectionsiximage3details = models.TextField(null=True,blank=True)
      sectionsiximage4details = models.TextField(null=True,blank=True)
      sectionsiximage5details = models.TextField(null=True,blank=True)
      sectionsiximage6details = models.TextField(null=True,blank=True)
      sectionsiximage1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionsiximage1')
      sectionsiximage2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionsiximage2')
      sectionsiximage3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionsiximage3')
      sectionsiximage4 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionsiximage4')
      sectionsiximage5 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionsiximage5')
      sectionsiximage6 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionsiximage6')
      page = models.ForeignKey(Whyus, on_delete=models.CASCADE,null=True,blank=True,related_name='Whyussectionsix')

      def __str__(self):
          return f'Whyussectionsix'

class Whyussectionfive(models.Model):
      sectionfivetopheading = models.TextField(null=True,blank=True)
      sectionfivesubheading = models.TextField(null=True,blank=True)
      sectionfivediscription = models.TextField(null=True,blank=True)
      sectionfiveheading = models.TextField(null=True,blank=True)
      sectionfivetopsubheading = models.TextField(null=True,blank=True)
      sectionfivecolourtext = models.TextField(null=True,blank=True)
      sectionfiveimage1details = models.TextField(null=True,blank=True)
      sectionfiveimage2details= models.TextField(null=True,blank=True)
      sectionfiveimage3details = models.TextField(null=True,blank=True)
      sectionfiveimage1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionfiveimage1')
      sectionfiveimage2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionfiveimage2')
      sectionfiveimage3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionfiveimage3')
      page = models.ForeignKey(Whyus, on_delete=models.CASCADE,null=True,blank=True,related_name='Whyussectionfive')

      def __str__(self):
          return f'Whyussectionfive'



class Whyussectionthree(models.Model):
      sectiononeheading = models.TextField(null=True,blank=True)
      sectiononesubheading = models.TextField(null=True,blank=True)
      sectiononediscription = models.TextField(null=True,blank=True)
      sectionthreevideoimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionthreevideoimg')
      sectionthreevideo = models.ForeignKey(VideoBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectionthreevideo')
      page = models.ForeignKey(Whyus, on_delete=models.CASCADE,null=True,blank=True,related_name='Whyussectionthree')

      def __str__(self):
          return f'Whyussectionthree'

class Whyussectiontwo(models.Model):
      sectiontwoheading = models.TextField(null=True,blank=True)
      sectiontwosubheading = models.TextField(null=True,blank=True)
      sectiontwodiscription = models.TextField(null=True,blank=True)
      sectiontwobtntext = models.TextField(null=True,blank=True)
      sectiontwobtnurl = models.TextField(null=True,blank=True)
      sectiontwoimage1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectiontwoimage1')
      sectiontwoimage2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='whyussectiontwoimage2')
      page = models.ForeignKey(Whyus, on_delete=models.CASCADE,null=True,blank=True,related_name='Whyussectiontwo')

      def __str__(self):
          return f'Whyussectiontwo'

# class whyusreview(models.Model):
#       username = models.TextField()
#       userdesignation = models.TextField()
#       userreview = models.TextField()
#       userphoto = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='whyusreviewuserphoto')
#       page = models.ForeignKey(Whyus, on_delete=models.CASCADE,null=True,blank=True,related_name='whyusreview')

#       def __str__(self):
#          return f'whyusreview'






# class Pricing(models.Model):

#       #     def remove_numbers(value):
#       #         return re.sub(r'\d', '', value)

#       title = models.TextField(null=True, blank=True, unique=True)
#       slug = AutoSlugField(populate_from='title', unique=True)

#       def __str__(self):
#             return self.title

#       def save(self, *args, **kwargs):
#             if self.title != self.slug:  # Only update the slug if the title has changed
#                   self.slug = slugify(self.title)
#             super().save(*args, **kwargs)



class Pricingsectionone(models.Model):
      sectiononeheading = models.TextField(null=True,blank=True)
      sectiononesubheading = models.TextField(null=True,blank=True)
      sectiononediscription = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Pricing, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionone')



      def __str__(self):
         return f'Pricingsectionone'

class Pricingsectiontwo(models.Model):
      sectiontwoheading = models.TextField(null=True,blank=True)
      sectiontwopoint1 = models.TextField(null=True,blank=True)
      sectiontwopoint2 = models.TextField(null=True,blank=True)
      sectiontwopoint3 = models.TextField(null=True,blank=True)
      sectiontwopoint4 = models.TextField(null=True,blank=True)
      sectiontwopoint5 = models.TextField(null=True,blank=True)
      sectiontwopoint6 = models.TextField(null=True,blank=True)
      sectiontwocompareprice = models.TextField(null=True,blank=True)
      sectiontwourl = models.TextField(null=True,blank=True)
      sectiontwocapability = models.TextField(null=True,blank=True)
      pricepdf = models.FileField(null=True,blank=True,upload_to='documents/')
      page = models.ForeignKey(Pricing, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectiontwo')



      def __str__(self):
         return f'Pricingsectiontwo'

class Pricingsectionthree(models.Model):
      sectionthreeheading = models.TextField(null=True,blank=True)
      sectionthreesubheading = models.TextField(null=True,blank=True)
      sectionthreediscription = models.TextField(null=True,blank=True)
      sectionthreetext = models.TextField(null=True,blank=True)
      sectionthreesubheading2 = models.TextField(null=True,blank=True)
      sectionthreeparagraph = models.TextField(null=True,blank=True)
      sectionthreevideoimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='sectionthreevideoimg')
      page = models.ForeignKey(Pricing, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionthree')
      sectionthreevideo = models.ForeignKey(VideoBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionthreevideo')


      def __str__(self):
         return f'Pricingsectionthree'


# class Pricinguserreview(models.Model):
#       username = models.TextField()
#       userdesignation = models.TextField()
#       userreview = models.TextField()
#       userphoto = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='pricinguserphoto')
#       page = models.ForeignKey(Pricing, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricinguserreview')

#       def __str__(self):
#          return f'Pricinguserreview'

class PricingFaq(models.Model):
      question = models.TextField()
      answer = models.TextField()

      page = models.ForeignKey(Pricing, on_delete=models.CASCADE,null=True,blank=True,related_name='PricingFaq')

      def __str__(self):
         return f'PricingFaq'

class Pricingsectionfour(models.Model):
      sectionfourheading = models.TextField(null=True,blank=True)
      sectionfoursubheading = models.TextField(null=True,blank=True)
      sectionfourparagraph = models.TextField(null=True,blank=True)
      sectionfourpoint1 = models.TextField(null=True,blank=True)
      sectionfourpoint2 = models.TextField(null=True,blank=True)
      sectionfourpoint3 = models.TextField(null=True,blank=True)
      sectionfourpoint4 = models.TextField(null=True,blank=True)
      sectionfourimage1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionfourimage1')
      sectionfourimage2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionfourimage2')
      sectionfourimage3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionfourimage3')
      sectionfourimage4 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionfourimage4')
      sectionfourimage5 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionfourimage5')
      sectionfourimage6 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionfourimage6')
      page = models.ForeignKey(Pricing, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingsectionfour')

      def __str__(self):
         return f'Pricingsectionfour'


class Pricingdetails(models.Model):
      pricingtag = models.TextField(null=True,blank=True)
      pricingheading = models.TextField(null=True,blank=True)
      pricingsubheading = models.TextField(null=True,blank=True)
      pricingparagraph = models.TextField(null=True,blank=True)
      pricingsimpletext = models.TextField(null=True,blank=True)
      pricingbtntext = models.TextField(null=True,blank=True)
      pricingbtnurl = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Pricing,null=True,blank=True, on_delete=models.CASCADE,related_name='Pricingdetails')

      def __str__(self):
         return f'Pricingdetails'




class Pricingsubdetails(models.Model):
      pricingsubtag = models.BooleanField(default=True)
      pricingheading = models.TextField()
      pricingpage = models.ForeignKey(Pricingdetails,null=True,blank=True, on_delete=models.CASCADE,related_name='pricingpage')

      def __str__(self):
         return f'Pricingsubdetails'


class Pricingcta(models.Model):
      Pricingctaheading = models.TextField(null=True,blank=True)
      Pricingctasubheading = models.TextField(null=True,blank=True)
      Pricingctabtntext = models.TextField(null=True,blank=True)
      Pricingctabtnurl = models.TextField(null=True,blank=True)
      Pricingctaimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='pricingctaimg')
      Pricingctamobileimg = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='pricingctaimage2')
      page = models.ForeignKey(Pricing, on_delete=models.CASCADE,null=True,blank=True,related_name='Pricingcta')

      def __str__(self):
          return f'Pricingcta'

class Blogauthor(models.Model):
    profilephoto = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='profilephoto')
    bio = models.TextField()
    Position = models.TextField()
    name = models.CharField(max_length=225,unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name != self.slug:  # Only update the slug if the title has changed
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tag(models.Model):
    tag = models.TextField(unique=True)
    slug = AutoSlugField(populate_from='tag', unique=True)


    def __str__(self):
        return self.tag

    def save(self, *args, **kwargs):
        if self.tag != self.slug:  # Only update the slug if the title has changed
            self.slug = slugify(self.tag)
        super().save(*args, **kwargs)


class BlogPost(models.Model):
      title = models.CharField(max_length=800, unique=True)
      slug = AutoSlugField(populate_from='title', unique=True)
      category = models.CharField(max_length=800,null=True,blank=True)
      thumbnail = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='blogpostthumbnail')
      Postauthor = models.ForeignKey(Blogauthor, on_delete=models.CASCADE,related_name='blogpostauthor')
      body = RichTextUploadingField()
      summary = models.TextField()
      created = models.DateTimeField(auto_now_add=True)
      tag = models.ManyToManyField(Tag, related_name='blogposts')
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='servicesBlogPost')


      def __str__(self):
            return self.title

      def save(self, *args, **kwargs):
            if self.title != self.slug:  # Only update the slug if the title has changed
                  self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class Ourworkproject(models.Model):
      title = models.CharField(max_length=800, unique=True)
      slug = AutoSlugField(populate_from='title', unique=True)
      projectsummary = models.TextField()
      year = models.IntegerField()
      industry = models.TextField()
      projectthumbnail = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='projectthumbnailourwork')
      body = RichTextUploadingField()
      created = models.DateTimeField(auto_now_add=True)
      page = models.ForeignKey(Page, on_delete=models.CASCADE,null=True,blank=True,related_name='servicesourwork')


      def __str__(self):
            return self.title

      def save(self, *args, **kwargs):
            if self.title != self.slug:  # Only update the slug if the title has changed
                  self.slug = slugify(self.title)
            super().save(*args, **kwargs)




#################


class Bookacall(models.Model):


      title = models.TextField(null=True,blank=True,unique=True)
      slug = AutoSlugField(populate_from='title', unique=True)


      def __str__(self):
          return self.title

      def save(self, *args, **kwargs):
            if self.title != self.slug:  # Only update the slug if the title has changed
                  self.slug = slugify(self.title)
            super().save(*args, **kwargs)



class Bookacallsectionone(models.Model):
      sectiononeheading = models.TextField(null=True,blank=True)
      sectiononesubheading = models.TextField(null=True,blank=True)
      sectiononediscription = models.TextField(null=True,blank=True)
      sectiononeimg1 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='bookacallsectiononeimg1')
      sectiononeimg2 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='bookacallsectiononeimg2')
      sectiononeimg3 = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,null=True,blank=True,related_name='bookacallsectiononeimg3')
      page = models.ForeignKey(Bookacall, on_delete=models.CASCADE,null=True,blank=True,related_name='Bookacallsectionone')

      def __str__(self):
          return f'Bookacallsectionone'


class Bookacallsectiontwo(models.Model):
      sectiontwotext1 = models.TextField(null=True,blank=True)
      sectiontwosubheading1 = models.TextField(null=True,blank=True)
      sectiontwodiscription1 = models.TextField(null=True,blank=True)
      sectiontwotext2 = models.TextField(null=True,blank=True)
      sectiontwosubheading2 = models.TextField(null=True,blank=True)
      sectiontwodiscription2 = models.TextField(null=True,blank=True)
      sectiontwotext3 = models.TextField(null=True,blank=True)
      sectiontwosubheading3 = models.TextField(null=True,blank=True)
      sectiontwodiscription3 = models.TextField(null=True,blank=True)
      sectiontwotext4 = models.TextField(null=True,blank=True)
      sectiontwosubheading4 = models.TextField(null=True,blank=True)
      sectiontwodiscription4 = models.TextField(null=True,blank=True)
      sectiontwocopyrighttext = models.TextField(null=True,blank=True)
      page = models.ForeignKey(Bookacall, on_delete=models.CASCADE,null=True,blank=True,related_name='Bookacallsectiontwo')

      def __str__(self):
          return f'Bookacallsectiontwo'


# class BookacallSlidersection1(models.Model):
#       sliderimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='bookacallsliderimagesection1')
#       page = models.ForeignKey(Bookacall, on_delete=models.CASCADE,null=True,blank=True,related_name='BookacallSlidersection1')

#       def __str__(self):
#          return f'BookacallSlidersection1'


# class BookacallSlidersection2(models.Model):
#       sliderimage = models.ForeignKey(MediaBucket, on_delete=models.CASCADE,related_name='bookacallsliderimagesection2')
#       page = models.ForeignKey(Bookacall, on_delete=models.CASCADE,null=True,blank=True,related_name='BookacallSlidersection2')

#       def __str__(self):
#          return f'BookacallSlidersection2'

class Emailinput(models.Model):
      email = models.TextField(unique=True)


      def __str__(self):
         return self.email

class Social(models.Model):
      social = models.TextField(unique=True)
      socialurl = models.TextField(unique=True)

      def __str__(self):
         return self.social


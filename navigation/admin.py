from django.contrib import admin
from .models import *


model_list = [ MediaBucket,Header,Menu,SubMenu,Footer,Sectiontwo,Sectionfour,Sectionone,VideoBucket,Sectionthree,Details,Pricingsubdetails,Emailinput,Social,
    Bookacall,Bookacallsectionone,Bookacallsectiontwo,Facts,Pricingcta,Servicessectionfour,servicescapabilities,Servicescta,Userdata,Homepagemeta,Pricingmeta,Whyusmeta,Ourworkmeta,Blogsmeta,Servicesmeta,
    Page,Servicessectionone,Servicessectiontwo,ServicessectionThree,Faq,Servicessectionsix,Servicessectionseven,Pricingdetails,Ourwork,Ourworksectionone,Ourworksectiontwo,Blogs,Blogsectionone,Blogsectiontwo,Blogsectionthree,Blogsectionfour,Pricingsectionfour,CommonSlidersection2,CommonReview,CommonSlidersection1,
    Whyus,Whyussectionseven,Whyussectionsix,Whyussectionfive,Whyussectionthree,Homepage,Sectionfive,Singlereview,Sectionsix,Blogsectionfive,
    Whyussectiontwo,PricingFaq,Pricingsectionthree,Pricingsectiontwo,Pricingsectionone,Pricing,Tag,Blogauthor,BlogPost,Ourworkproject,Category,Subcategory,Commonbranding,Servicesblog]
# Register your models here.

for model in model_list:
    admin.site.register(model)







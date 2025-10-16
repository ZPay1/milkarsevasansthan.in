from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in Users._meta.fields]     

@admin.register(BankDetails)
class BankDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BankDetails._meta.fields]


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Slider._meta.fields]    


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gallery._meta.fields]



from django.contrib import admin
# from .models import AboutUs, AboutUsItem
from .models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AboutUs._meta.fields]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Certificate._meta.fields]

@admin.register(Awards)
class AwardAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Awards._meta.fields]


@admin.register(Ourteam)
class OurteamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ourteam._meta.fields]



@admin.register(ManagementMember)
class ManagementMemberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ManagementMember._meta.fields]

@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MissionVision._meta.fields]

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Donation._meta.fields]


from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.shortcuts import  redirect
from django.contrib import messages
from superadmin.models import *
from django.contrib.auth.hashers import check_password
from Users.models import *
'''
===============================================================================================================
                        Admin Login method
===============================================================================================================
'''
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Admin

from django.views.decorators.csrf import csrf_exempt

'''@csrf_exempt
def admin_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('Email', '').strip()
        print(f'{email=}')
        password = request.POST.get('password', '').strip()
        print(f'{password=}')
        admindt = Admin.objects.filter(admin_email=email).first()
        if admindt:  # user mila
            if password == str(admindt.admin_password): 
                request.session['admin_id'] = admindt.admin_id 
                return redirect('dashboard_view') 
            else: messages.error(request, 'Wrong password.') 
        
        else:
            messages.error(request, "Admin not found.")

    return render(request, 'superadmin/admin_login.html')
'''

@csrf_exempt
def admin_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('Email', '').strip()
        password = request.POST.get('password', '').strip()

        admindt = Admin.objects.filter(admin_email=email).first()
        if admindt:
            if check_password(password, admindt.admin_password):  
                # request.session['admin_id'] = admindt.admin_id 
                request.session['admin_id'] = admindt.admin_id
                return redirect('dashboard_view')
            else:
                messages.error(request, 'Wrong password.') 
        else:
            messages.error(request, "Admin not found.")

    return render(request, 'superadmin/admin_login.html')


'''
===============================================================================================================
                          Admin Logout method
===============================================================================================================
'''


from django.shortcuts import redirect
from django.contrib import messages

# def admin_logout_view(request):
#     request.session.flush()  
#     messages.success(request, "You have been logged out successfully.")
#     return redirect('admin_login')


def admin_logout_view(request):
 
    if 'admin_id' in request.session:
        del request.session['admin_id']
    
    # Optional: puri session clear karne ke liye
    request.session.flush()

    messages.success(request, "Logged out successfully!")
    return redirect('admin_login')  


'''
===============================================================================================================
                          Admin Dashboard method
===============================================================================================================
'''

def dashboard_view(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    # admin_id = request.session['admin_id']
    admin_id = request.session['admin_id']
    # print(f'{admin_id=}')
    profile = Admin.objects.filter(admin_id=admin_id).first()
    # print(f'{profile=}')
    context={
        'profile':profile
    }
    return render(request, 'superadmin/dashboard.html',context)


'''
===============================================================================================================
                            Admin Profile method
===============================================================================================================
'''


from .models import Admin  

def profile_view(request):
    admin_id = request.session['admin_id']
    # print(f'{admin_id=}')
    profile = Admin.objects.filter(admin_id=admin_id).first()
    # print(f'{profile=}')
    return render(request, 'superadmin/profile.html', {'profile': profile})


'''
===============================================================================================================
                        Admin Slider method
===============================================================================================================
'''
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import SliderForm


# List all sliders
def slider_view(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    sliders = Slider.objects.filter(is_deleted=False)
    return render(request, "superadmin/slider_list.html", {"sliders": sliders})


# Add new slider
def slider_add(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    if request.method == "POST":
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Slider added successfully!")
            return redirect("slider_view")
    else:
        form = SliderForm()
    return render(request, "superadmin/slider_form.html", {"form": form, "title": "Add Slider"})


def slider_edit(request, slider_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    slider = get_object_or_404(Slider, pk=slider_id)
    if request.method == "POST":
        form = SliderForm(request.POST, request.FILES, instance=slider)
        if form.is_valid():
            form.save()
            messages.success(request, "Slider updated successfully!")
            return redirect("slider_view")
    else:
        form = SliderForm(instance=slider)
    return render(request, "superadmin/slider_form.html", {"form": form, "title": "Edit Slider"})



def slider_delete(request, slider_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    slider = get_object_or_404(Slider, pk=slider_id)
    slider.is_deleted = True
    slider.save()
    messages.success(request, "Slider deleted successfully!")
    return redirect("slider_view")

'''
===============================================================================================================
                            Admin Gallery Image method
===============================================================================================================
'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import GalleryForm

# List View
def gallery_list(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    galleries = Gallery.objects.filter(is_deleted=False)
    return render(request, "superadmin/gallery_list.html", {"galleries": galleries})


# Add View
def gallery_add(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image added to gallery successfully!")
            return redirect("gallery_list")
    else:
        form = GalleryForm()
    return render(request, "superadmin/gallery_form.html", {"form": form, "title": "Add Gallery Image"})


# Edit/Update View
def gallery_edit(request, gallery_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    gallery = get_object_or_404(Gallery, id=gallery_id)
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            messages.success(request, "Gallery image updated successfully!")
            return redirect("gallery_list")
    else:
        form = GalleryForm(instance=gallery)
    return render(request, "superadmin/gallery_form.html", {"form": form, "title": "Edit Gallery Image"})



# Delete (Soft Delete)
def gallery_delete(request, gallery_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    gallery = get_object_or_404(Gallery, id=gallery_id)
    gallery.is_deleted = True
    gallery.save()
    messages.success(request, "Gallery image deleted successfully!")
    return redirect("gallery_list")



'''
===============================================================================================================
                            Contact Us method
===============================================================================================================
'''
def contactus_view(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    contact_us = Contact.objects.filter(is_deleted=False)
    # print(f'{contact_us=}')
    return render(request, 'superadmin/contact_list.html', {"contact_us": contact_us})


'''
===============================================================================================================
                            Certificate method
===============================================================================================================
'''
from .forms import CertificateForm

def certificate_list(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    certificate = Certificate.objects.filter(is_deleted=False)
    # print(f'{certificate=}')
    return render(request, 'superadmin/certificate_list.html', {"certificate": certificate})



def certificate_add(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    if request.method == "POST":
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "certificate added successfully!")
            return redirect("certificate_list")
    else:
        form = CertificateForm()
    return render(request, "superadmin/certificate_form.html", {"form": form, "title": "Add Certificate "})
   


def certificate_edit(request,c_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    certificate = get_object_or_404(Certificate, id=c_id)
    if request.method == "POST":
        form = CertificateForm(request.POST, request.FILES, instance=certificate)
        if form.is_valid():
            form.save()
            messages.success(request, "Certificate  updated successfully!")
            return redirect("certificate_list")
    else:
        form = CertificateForm(instance=certificate)
    return render(request, "superadmin/certificate_form.html", {"form": form, "title": "Edit Certificate "})
    
    
def certificate_delete(request,c_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    certificate = get_object_or_404(Certificate, id=c_id)
    certificate.is_deleted = True
    certificate.save()
    messages.success(request, "certificate  deleted successfully!")
    return redirect("certificate_list")

'''
===============================================================================================================
                        Awards & Achevements method
===============================================================================================================
'''
from .forms import AwardsForm

def award_achievements_list(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    Award_achievements = Awards.objects.filter(is_deleted=False)
    return render(request, 'superadmin/awards_achievement_list.html', {"Award_achievements": Award_achievements})



def award_achievements_add(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    if request.method == "POST":
        form = AwardsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Award & achievements added successfully!")
            return redirect("award_achievements_list")
    else:
        form = AwardsForm()
    return render(request, "superadmin/award_achievements_form.html", {"form": form, "title": "Add Award & achievements"})
   


def award_achievements_edit(request,achieve_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    achievement_awards = get_object_or_404(Awards, id=achieve_id)
    if request.method == "POST":
        form = AwardsForm(request.POST, request.FILES, instance=achievement_awards)
        if form.is_valid():
            form.save()
            messages.success(request, "Achievement & awards  updated successfully!")
            return redirect("award_achievements_list")
    else:
        form = AwardsForm(instance=achievement_awards)
 
    return render(request, 'superadmin/award_achievements_form.html', {"form": form, "title": "Edit Achievement & awards "})



def award_achievements_delete(request,achieve_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    achievement_awards = get_object_or_404(Awards, id=achieve_id)
    achievement_awards.is_deleted = True
    achievement_awards.save()
    messages.success(request, "achievement and awards  deleted successfully!")
    return redirect("award_achievements_list")


'''
===============================================================================================================
                       Our team method
===============================================================================================================
'''
from .forms import OurteamForm

def ourteam_list(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    ourteam = Ourteam.objects.filter(is_deleted=False)
    return render(request, 'superadmin/ourteam_list.html', {"ourteam": ourteam})



def ourteam_add(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    if request.method == "POST":
        form = OurteamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Team member added successfully!")
            return redirect("ourteam_list")
    else:
        form = OurteamForm()
    return render(request, "superadmin/ourteam_form.html", {"form": form, "title": "Add team member "})
   

def ourteam_edit(request,team_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    ourteam = get_object_or_404(Ourteam, id=team_id)
    if request.method == "POST":
        form = OurteamForm(request.POST, request.FILES, instance=ourteam)
        if form.is_valid():
            form.save()
            messages.success(request, "Team member updated successfully!")
            return redirect("ourteam_list")
    else:
        form = OurteamForm(instance=ourteam)
 
    return render(request, 'superadmin/ourteam_form.html', {"form": form, "title": "Edit team memeber"})




def ourteam_delete(request,team_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    ourteam = get_object_or_404(Ourteam, id=team_id)
    ourteam.is_deleted = True
    ourteam.save()
    messages.success(request, "Team member deleted successfully!")
    return redirect("ourteam_list")


'''
===============================================================================================================
                    Management method
===============================================================================================================
'''
from .forms import ManagementmembertForm

def managementMember_list(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    management = ManagementMember.objects.filter(is_deleted=False)
    return render(request, 'superadmin/management_member_list.html', {"management": management})



def managementMember_add(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    if request.method == "POST":
        form = ManagementmembertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Management member added  successfully!")
            return redirect("managementMember_list")
    else:
        form = ManagementmembertForm()
    return render(request, "superadmin/management_member_form.html", {"form": form, "title": "Add Management member "})
   


def managementMember_edit(request,management_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    management = get_object_or_404(ManagementMember, id=management_id)
    if request.method == "POST":
        form = ManagementmembertForm(request.POST, request.FILES, instance=management)
        if form.is_valid():
            form.save()
            messages.success(request, "Management member updated successfully!")
            return redirect("managementMember_list")
    else:
        form = ManagementmembertForm(instance=management)
 
    return render(request, 'superadmin/management_member_form.html', {"form": form, "title": "Edit Management member "})


def managementMember_delete(request,management_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    ourteam = get_object_or_404(ManagementMember, id=management_id)

    ourteam.is_deleted = True
    ourteam.save()
    messages.success(request, "Management member  deleted successfully!")
    return redirect("managementMember_list")


'''
===============================================================================================================
                    Mission & Vision method
===============================================================================================================
'''
from .forms import MissionvisionForm

def MissionVision_list(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    mission = MissionVision.objects.filter(is_deleted=False)
    return render(request, 'superadmin/mission_vision_list.html', {"mission": mission})


def MissionVision_add(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    if request.method == "POST":
        form = MissionvisionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Mission & Vision added  successfully!")
            return redirect("MissionVision_list")
    else:
        form = MissionvisionForm()
    return render(request, "superadmin/mission_vision_form.html", {"form": form, "title": "Add Mission & Vision  "})


def MissionVision_edit(request,mission_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    mission_vision = get_object_or_404(MissionVision, id=mission_id)
    if request.method == "POST":
        form = MissionvisionForm(request.POST, request.FILES, instance=mission_vision)
        if form.is_valid():
            form.save()
            messages.success(request, " Mission & Vision updated successfully!")
            return redirect("MissionVision_list")
    else:
        form = MissionvisionForm(instance=mission_vision)
 
    return render(request, 'superadmin/mission_vision_form.html', {"form": form, "title": "Edit Mission & Vision  "})


def MissionVision_delete(request,mission_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    ourteam = get_object_or_404(MissionVision, id=mission_id)
    ourteam.is_deleted = True
    ourteam.save()
    messages.success(request, "Mission & Vision  deleted successfully!")
    return redirect("MissionVision_list")


'''
===============================================================================================================
                    Donation method
===============================================================================================================
'''

def donation_list(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    donation = Donation.objects.filter(is_deleted=False)
    return render(request, 'superadmin/donation_list.html', {"donation": donation})
'''
===============================================================================================================
                            About Us method
===============================================================================================================
'''

from .forms import AboutUsForm

def aboutus_list(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    sections = AboutUs.objects.filter(is_deleted=False)
    # print(f'{sections=}')
    return render(request, "superadmin/aboutus_list.html",{'sections':sections})


def aboutus_add(request):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "About Us Section added successfully!")
            return redirect("aboutus_list")
    else:
        form = AboutUsForm()
      
    return render(request, "superadmin/aboutus_form.html", {"form": form, "title": "Add  About Us Section"})


def aboutus_edit(request, about_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
    
    section = get_object_or_404(AboutUs, pk=about_id)
    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, "About us Section updated successfully!")
            return redirect("aboutus_list")
    else:
        form = AboutUsForm(instance=section)
    return render(request, "superadmin/aboutus_form.html", {"form": form, "title": " Edit  About us Section"})


def aboutus_delete(request, about_id):
    if 'admin_id' not in request.session: 
        return redirect('admin_login')  
        
    # section = get_object_or_404(AboutUs, pk=about_id)
    section = get_object_or_404(AboutUs, pk=about_id)
    section.is_deleted = True
    section.save()
    messages.success(request, "About Us Section deleted successfully!")
    return redirect("aboutus_list")




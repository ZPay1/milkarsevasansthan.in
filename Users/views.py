from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.shortcuts import  redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Users, generate_unique_userid
import re
from django.contrib.auth.hashers import check_password
from .models import Users
from django.db.models import Q


def quick_links_view(request):
    return render(request, 'quick_links.html')


def goals_view(request):
    return render(request, 'goals.html')



'''
===============================================================================================================
                                    User Login method
===============================================================================================================
'''
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == "POST": 
        identifier = request.POST.get("email") 
        password = request.POST.get("password")
        remember = request.POST.get("remember")  

        try:
            # Check if user exists by email OR mobile
            user = Users.objects.get(Q(email=identifier) | Q(mobile=identifier))
            
            if not user.is_active:
                messages.error(request, "Your account is deactivated. Contact admin.")
                return redirect('login_view')

            # Verify password
            if check_password(password, user.password):
                # Login successful
                request.session['user_id'] = user.userid
                request.session['username'] = user.username

                # Remember me functionality
                if remember:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
                    request.session.set_expiry(0)  # Browser close

                messages.success(request, f"Welcome {user.username}!")
                return redirect('homepage_view')
            else:
                messages.error(request, "Incorrect password.")
                return redirect('login_view')

        except Users.DoesNotExist:
            messages.error(request, "User not found. Please signup first.")
            return redirect('signup_view')

    # GET request: show login form
    return render(request, 'login.html')

'''
===============================================================================================================
                            Logout method
===============================================================================================================
'''
def logout_view(request):
    if 'user_id' not in request.session:
        return redirect('login_view')
    
    user_id = request.session.get('user_id')
    print('Logging out user:', user_id)
    
    # Remove session data
    request.session.flush() 
    messages.success(request, "Logged out successfully!")
    return redirect('login_view')

'''
===============================================================================================================
                                    Signup method
===============================================================================================================
'''


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")

        # ---------- Validations ----------

        # Username validation
        if len(username) < 4:
            messages.error(request, "Username must be at least 4 characters.")
            return redirect('signup_view')

        # Email validation using regex
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            messages.error(request, "Invalid email address.")
            return redirect('signup_view')

        # Mobile validation: 10 digits
        if not mobile.isdigit() or len(mobile) != 10:
            messages.error(request, "Mobile number must be 10 digits.")
            return redirect('signup_view')

        # Check if email or mobile already exists
        if Users.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup_view')
        if Users.objects.filter(mobile=mobile).exists():
            messages.error(request, "Mobile number already registered")
            return redirect('signup_view')

        # ---------- Create new user ----------
        user = Users(
            userid = generate_unique_userid(),
            username = username,
            email = email,
            mobile = mobile,
            password = make_password(password),  
        )
        user.save()

        messages.success(request, "Signup successful! Please login.")
        return redirect('login_view')

    return render(request, "signup.html")





'''
===============================================================================================================
                                  Homepage method
===============================================================================================================
'''

def homepage_view(request):
     
    # if 'user_id' not in request.session:  
    #     return redirect('login_view')  

    sliders = Slider.objects.filter(is_active=True, is_deleted=False)
    # print(f'{sliders=}')
    slider_images = [slide.image.url for slide in sliders if slide.image]
    gallery_images = Gallery.objects.filter(is_active=True,is_deleted=False )
    team = Ourteam.objects.filter(is_active=True,is_deleted=False )
    members = ManagementMember.objects.filter(is_active=True,is_deleted=False)
    donations = Donation.objects.filter(is_active=True).order_by("-created_at")
    aboutus = AboutUs.objects.filter(is_active=True,is_deleted=False )

 
    context={
        'aboutus':aboutus,
        'sliders': sliders,
        'slider_images': slider_images,
        'gallery_images': gallery_images,
        'team':team,
        'members':members,
        'donations':donations
    }
    return render(request, 'homepage.html', context)



'''
===============================================================================================================
                                    Slider method
===============================================================================================================
'''
from .models import *
def slider_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    sliders = Slider.objects.filter(is_active=True, is_deleted=False)
    # print(f'{sliders=}')
    return render(request, 'slider.html', {'sliders': sliders})

'''
===============================================================================================================
                                    Slider Image method
===============================================================================================================
'''
def banner_image_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    sliders_image = Slider.objects.filter(is_active=True, is_deleted=False)
    return render(request, 'slider_images.html', {'sliders_image': sliders_image})



'''
===============================================================================================================
                                    Our Gallery method
===============================================================================================================
'''
def gallery_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    gallery_images = Gallery.objects.filter(is_active=True,is_deleted=False )
  
    return render(request, 'gallery.html', {'gallery_images': gallery_images})


 
'''
===============================================================================================================
                               Photo Gallery method
===============================================================================================================
'''


def photo_gallery_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    
    # images = Gallery.objects.all()
    images = Gallery.objects.filter(is_active=True,is_deleted=False )
    return render(request, "photo_gallery.html", {"images": images})

'''
===============================================================================================================
                                    About Us method
===============================================================================================================
'''

from django.shortcuts import render
def aboutus_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    
    aboutus = AboutUs.objects.filter(is_active=True,is_deleted=False )
    context={
        'aboutus':aboutus,
      
    }
    return render(request, 'aboutus.html',context)


'''
===============================================================================================================
                                    Mission & Vision method
===============================================================================================================
'''
def mission_vision_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    mission_vision = MissionVision.objects.filter(is_active=True,is_deleted=False )
    return render(request, 'mission_vision.html',{'mission_vision':mission_vision})


'''
===============================================================================================================
                                Our Management body method
===============================================================================================================
'''
def management_body_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    members = ManagementMember.objects.filter(is_active=True,is_deleted=False)
    return render(request, 'management_body.html',{'members':members})



'''
===============================================================================================================
                                Our Team method
===============================================================================================================
'''
def team_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    team = Ourteam.objects.filter(is_active=True,is_deleted=False )
    return render(request, 'team.html',{'team':team})

'''
===============================================================================================================
                                Achievement method
===============================================================================================================
'''
def achievement_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    achievement = Awards.objects.filter(is_active=True,is_deleted=False )
    return render(request, 'achievement.html',{'achievement':achievement})


'''
===============================================================================================================
                               Certificate method
===============================================================================================================
'''
def certificate_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    certificate = Certificate.objects.filter(is_active=True,is_deleted=False )
    return render(request, 'certificate.html',{'certificate':certificate})



'''
===============================================================================================================
                               Our project method
===============================================================================================================
'''
def project_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
 
    return render(request, 'project.html')



'''
===============================================================================================================
                               Contact Us method
===============================================================================================================
'''

from django.core.mail import send_mail
from django.conf import settings
import logging

def contact_us_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        print(email)
        mobile = request.POST.get('mobile')
        print(mobile)
        message = request.POST.get('message')
        print(mobile)
        
     # Mobile validation (10 digits only)
        if not re.fullmatch(r'[6-9]\d{9}', mobile):
            messages.error(request, "Please enter a valid 10-digit mobile number starting with 6-9.")
            return redirect('contact_us')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            message=message
        )
        
        try:
            send_mail(
                subject="Thank You for Contacting Us",
                message=f"Hi {name},\n\nThank you for reaching out. We have received your message and will get back to you shortly.\n\nRegards,\nTeam",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            print("send mail")
        except Exception as e:
             print(f'{e=}')
             pass #  (f"Error sending confirmation email: {e}")

        messages.success(request, 'Thank you for your enquiry! We will get back to you soon.')
        return redirect('contact_us')

    return render(request, 'contact_us.html')

'''
===============================================================================================================
                    Donate Us method
===============================================================================================================
'''
from django.db import transaction
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal


def donate_us_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        amount = request.POST.get("amount")
        pan_number = request.POST.get("pan_number")
        bank_name = request.POST.get("bank_name")
        branch_name = request.POST.get("branch_name")
        account_number = request.POST.get("account_number")
        ifsc_code = request.POST.get("ifsc_code")

        try:
            with transaction.atomic():
                # Check if user exists by email
                user, created = Users.objects.get_or_create(
                    email=email,
                    defaults={
                        'userid': generate_unique_userid(),
                        'username': username,
                        'mobile': mobile,
                        'address': address,
                        'amount': amount
                    }
                )

                # If user already exists, you can update the amount
                if not created:
                    user.amount += Decimal(amount)
                    user.save()

                # Create or update BankDetails
                BankDetails.objects.update_or_create(
                    user=user,
                    defaults={
                        'pan_number': pan_number,
                        'bank_name': bank_name,
                        'branch_name': branch_name,
                        'account_number':account_number,
                        'ifsc_code':ifsc_code

                    }
                )

            messages.success(request, "Donation successful! Thank you.")
            return redirect('homepage_view')

        except Exception as e:
            print(f"Error saving donation: {e}")
            messages.error(request, "Something went wrong. Please try again.")
            return redirect('donate_us_view')

    return render(request, 'donate_us_form.html')


'''
===============================================================================================================
                    Donate Us method
===============================================================================================================
'''
from django.shortcuts import render
from .models import Donation

def donor_name_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    
    donations = Donation.objects.filter(is_active=True).order_by("-created_at")
    return render(request, "donation_popup.html", {"donations": donations})
#     return render(request,'header.html')



'''
===============================================================================================================
                    Footer method
===============================================================================================================
'''
def term_condition_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    return render(request, 'term_condition.html')


def return_policy_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    return render(request, 'return_policy.html')


def privacy_policy_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    return render(request, 'privacy_policy.html')


def disclaimer_view(request):
    return render(request, 'disclaimer.html')


def refund_policy_view(request):
    if 'user_id' not in request.session:  
        return redirect('login_view')  
    return render(request, 'refund_policy.html')



from . import views
from django.contrib import admin
from django.urls import path
urlpatterns = [
   
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('log-out/', views.logout_view, name='logout_view'),
    path('', views.homepage_view, name='homepage_view'),
    path('slider/', views.slider_view, name='slider_view'),
    path('banner-images/', views.banner_image_view, name='banner_image_view'),
    path('gallery/', views.gallery_view, name='gallery_view'),
    path('about-us/', views.aboutus_view, name='aboutus_view'),
    path('mission-vision/', views.mission_vision_view, name='mission_vision_view'),
    path('our-management-body/', views.management_body_view, name='management_body_view'),
    path('our-team/', views.team_view, name='team_view'),
    path('achievements/', views.achievement_view, name='achievement_view'),
    path('certificates/', views.certificate_view, name='certificate_view'),
    path('our-project/', views.project_view, name='project_view'),
    path('photo-gallery/', views.photo_gallery_view, name='photo_gallery_view'),
    path('contact-us/', views.contact_us_view, name='contact_us'),
 
    path('quick-links/', views.quick_links_view, name='quick_links_view'),
    path('goals/', views.goals_view, name='goals_view'),
    # path('login/', views.login_view, name='login_view')
    
    path('donate-us/', views.donate_us_view, name='donate_us_view'),
    path('donation-name/', views.donor_name_view, name='donor_name_view'),

    path('term-condition/', views.term_condition_view, name='term_condition'),
    path('return-policy/', views.return_policy_view, name='return_policy'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('disclaimer/', views.disclaimer_view, name='disclaimer_view'),
    path('refund-policy/', views.refund_policy_view, name='refund_policy'),

    
]
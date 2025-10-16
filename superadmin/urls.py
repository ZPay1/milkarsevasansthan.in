from . import views
from django.contrib import admin
from django.urls import path
urlpatterns = [   
    # Login/Dashboard url  =========================================
    path('', views.admin_login_view, name='admin_login'),
    path('logout', views.admin_logout_view, name='admin_logout'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
  
    # Slider url  =========================================
    path("sliders/", views.slider_view, name="slider_view"),
    path("sliders/add/", views.slider_add, name="slider_add"),
    path("sliders/edit/<int:slider_id>/", views.slider_edit, name="slider_edit"),
    path("sliders/delete/<int:slider_id>/", views.slider_delete, name="slider_delete"),
   
    # Gallery url  =========================================
    path("gallery/", views.gallery_list, name="gallery_list"),
    path("gallery/add/", views.gallery_add, name="gallery_add"),
    path("gallery/edit/<int:gallery_id>/", views.gallery_edit, name="gallery_edit"),
    path("gallery/delete/<int:gallery_id>/", views.gallery_delete, name="gallery_delete"),

    # Contact us url  =========================================
    path("contact-us/", views.contactus_view, name="contactus"),

    # Certificate us url  =========================================
    path("certificate/", views.certificate_list, name="certificate_list"),
    path("certificate/add/", views.certificate_add, name="certificate_add"),
    path("certificate/edit/<int:c_id>/", views.certificate_edit, name="certificate_edit"),
    path("certificate/delete/<int:c_id>/", views.certificate_delete, name="certificate_delete"),

    # Awards and Achievements  url  =========================================
    path("achievements/", views.award_achievements_list, name="award_achievements_list"),
    path("achievements/add/", views.award_achievements_add, name="award_achievements_add"),
    path("achievements/edit/<int:achieve_id>/", views.award_achievements_edit, name="award_achievements_edit"),
    path("achievements/delete/<int:achieve_id>/", views.award_achievements_delete, name="award_achievements_delete"),

    # Our team url  =========================================
    path("ourteam/", views.ourteam_list, name="ourteam_list"),
    path("ourteam/add/", views.ourteam_add, name="ourtam_add"),
    path("ourteam/edit/<int:team_id>/", views.ourteam_edit, name="ourteam_edit"),
    path("ourteam/delete/<int:team_id>/", views.ourteam_delete, name="ourteam_delete"),

   # Management body url  =========================================
    path("management-memebr/", views.managementMember_list, name="managementMember_list"),
    path("management-member/add/", views.managementMember_add, name="managementMember_add"),
    path("management-member/edit/<int:management_id>/", views.managementMember_edit, name="managementMember_edit"),
    path("management-member/delete/<int:management_id>/", views.managementMember_delete, name="managementMember_delete"),

    # Mission/Vision url  =========================================
    path("mission-vision/", views.MissionVision_list, name="MissionVision_list"),
    path("mission-vision/add/", views.MissionVision_add, name="MissionVision_add"),
    path("mission-vision/edit/<int:mission_id>/", views.MissionVision_edit, name="MissionVision_edit"),
    path("mission-vision/delete/<int:mission_id>/", views.MissionVision_delete, name="MissionVision_delete"),
    # Mission/Vision url  =========================================
    path("donation/", views.donation_list, name="donation_list"),

    
    # AboutUs section  =========================================
    path("aboutus/", views.aboutus_list, name="aboutus_list"),
    path("aboutus/add/", views.aboutus_add, name="aboutus_add"),
    path("aboutus/edit/<int:about_id>/", views.aboutus_edit, name="aboutus_edit"),
    path("aboutus/delete/<int:about_id>/", views.aboutus_delete, name="aboutus_delete"),
    path("profile/", views.profile_view, name="profile_view"),
    

  
]
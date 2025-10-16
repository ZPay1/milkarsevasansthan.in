from django.db import models

# Create your models here.
import random
import string
from django.db import models

'''
===============================================================================================================
                                User model
===============================================================================================================
'''
from django.contrib.auth.hashers import make_password
def generate_unique_userid():
    prefix = "MS"
    while True:
        # 7 characters after prefix to make total 10 characters
        suffix = ''.join(random.choices(string.digits, k=9))
        userid = prefix + suffix
        if not Users.objects.filter(userid=userid).exists():
            return userid

class Users(models.Model):
    userid = models.CharField(max_length=10, unique=True, editable=False ,db_index=True)
    username = models.CharField(max_length=100 ,db_index=True)
    mobile = models.CharField(max_length=15 ,db_index=True)
    email = models.EmailField(unique=True,db_index=True )
    password = models.CharField(max_length=128 , db_index=True )
    address=models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    profile_image=models.ImageField( null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Active user
    date = models.DateTimeField(auto_now_add=True , db_index=True )
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    


    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        if not self.userid:
            self.userid = generate_unique_userid()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.userid}"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"              # singular name
        verbose_name_plural = "Users"  
'''
===============================================================================================================
                                User Bank Details model
===============================================================================================================
'''    
# Separate Bank Details Model
class BankDetails(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name="bank_details")
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    ifsc_code = models.CharField(max_length=11, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.bank_name or 'No Bank'}"
   
    
    
'''
===============================================================================================================
                            Slider model
===============================================================================================================
'''


class Slider(models.Model):
    title_small = models.CharField(max_length=100, help_text="Small heading, e.g., 'Welcome To'")
    title_large = models.CharField(max_length=200, help_text="Main heading, e.g., 'Milkar Seva Sansthan'")
    description = models.TextField()
    image = models.ImageField(upload_to='sliders/', help_text="Main slider image")
    logo = models.ImageField(upload_to='sliders/logos/', )
    is_active = models.BooleanField(default=True, help_text="Set True to show this slide")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title_large

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

'''
===============================================================================================================
                            Gallery model
===============================================================================================================
'''

class Gallery(models.Model):
    title = models.CharField(max_length=200,help_text="Image caption or title")
    image = models.ImageField(upload_to="gallery/", help_text="Upload gallery image")
    is_active = models.BooleanField(default=True, help_text="Show/Hide this image")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)


    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title if self.title else f"Gallery Image {self.id}"

    class Meta:
        verbose_name = "Gallery Image"              # singular name
        verbose_name_plural = "Gallery Images"

'''
===============================================================================================================
                            About Us model
===============================================================================================================
'''
''' About Us'''
class AboutUs(models.Model):
    title = models.CharField(max_length=200)   # e.g. About Milkar Seva Sansthan
    logo = models.ImageField(upload_to="about/")
    description = models.TextField()
    button_text = models.CharField(max_length=100, default="Know more About Us")
    is_active = models.BooleanField(default=True, help_text="Show/Hide this image")
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
  

    def __str__(self):
        return self.title



'''
===============================================================================================================
                        Contact tUs model
===============================================================================================================
'''
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=150, help_text="Full name of the user")
    email = models.EmailField(max_length=200, help_text="Email address of the user")
    mobile = models.CharField(max_length=15, help_text="Mobile number of the user")
    message = models.TextField(help_text="Message content from user")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the message was submitted")
    is_read = models.BooleanField(default=False, help_text="Mark True when admin reads the message")
    is_deleted = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.email}"



'''
===============================================================================================================
                        Certificate model
===============================================================================================================
'''

class Certificate(models.Model):
    title = models.CharField(max_length=200, help_text="Image caption or title")
    image = models.ImageField(upload_to="certificate/", help_text="Upload certificate image")
    button_text= models.CharField(max_length=100)
    is_active = models.BooleanField(default=True, help_text="Show/Hide this image")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)



'''
===============================================================================================================
                    Award model
===============================================================================================================
'''

from django.db import models

class Awards(models.Model):
    award_image = models.ImageField(upload_to="awards/", )
    title = models.CharField(max_length=255)  
    description = models.TextField()          
    years = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True, help_text="Show/Hide this image")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True )

    class Meta:
        ordering = ['-years'] 

    def __str__(self):
        return f"{self.title} ({self.years})"



'''
===============================================================================================================
                    Our Team model
===============================================================================================================
'''


from django.db import models

class Ourteam(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=50, choices=[
        ("member", "Member"),
        ("admin", "Admin"),
        ("sponsor", "Sponsor"),
    ])
    organization = models.CharField(max_length=200)
    # icon = models.CharField(max_length=50, default="fas fa-user-friends")
    # icon = models.ImageField(upload_to="ourteam/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True )

    def __str__(self):
        return f"{self.name} ({self.role})"


'''
===============================================================================================================
                        Management Body model
===============================================================================================================
'''
from django.db import models

class ManagementMember(models.Model):
    name = models.CharField(max_length=150)   
    designation = models.CharField(max_length=100)  
    organization = models.CharField(max_length=150)  
    # icon = models.CharField(max_length=50, default="fas fa-user-friends") 
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} ({self.designation})"

'''
===============================================================================================================
                        Mission/Vision model
===============================================================================================================
'''

from django.db import models

class MissionVision(models.Model):
    title = models.CharField(max_length=100)   
    description = models.TextField()          
    icon = models.CharField(max_length=50, help_text="FontAwesome class e.g. fas fa-book-reader")  
    is_active = models.BooleanField(default=True)      
    is_deleted = models.BooleanField(default=False, blank=True, null=True )
    class Meta:
        ordering = [ "id"]

    def __str__(self):
        return self.title




'''
===============================================================================================================
                        Donation model
===============================================================================================================
'''

class Donation(models.Model):
 
    # receipt_number = models.CharField(max_length=100, unique=True)  # Unique receipt no.
    # transaction_id = models.CharField(max_length=150, blank=True, null=True)  # Payment transaction id
    # payment_status = models.CharField(
    #     max_length=50,
    #     choices=[("pending", "Pending"), ("completed", "Completed"), ("failed", "Failed")],
    #     default="pending"
    # )
    # date = models.DateField()  
    # rupees_in_words = models.CharField(max_length=255, blank=True, null=True)  
    # address = models.TextField(blank=True, null=True)  
    # test = models.CharField(max_length=255, blank=True, null=True)  
    donor_name = models.CharField(max_length=150) 
    amount = models.CharField(max_length=50)      
    created_at = models.DateTimeField(auto_now_add=True)  
    
    is_active = models.BooleanField(default=True)   
    is_deleted = models.BooleanField(default=False, blank=True, null=True )
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.donor_name} - {self.amount}"

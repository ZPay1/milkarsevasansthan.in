from django.db import models
from django.db import models
import uuid
from django.contrib.auth.hashers import make_password

class Admin(models.Model):
    admin_id = models.CharField(max_length=8, unique=True, blank=True, default=uuid.uuid4().hex[:8])
    admin_name = models.CharField(max_length=50, blank=True, null=True)
    admin_email = models.EmailField(blank=True, null=True)
    admin_password = models.CharField(max_length=125,blank=True, null=True)
    admin_phone_number = models.CharField(max_length=15,blank=True, null=True)
    admin_verify_code = models.CharField(max_length=15,blank=True, null=True)
    profile_image=models.ImageField( null=True, blank=True)
    is_staff= models.BooleanField(default=False)   
    # is_active = models.BooleanField(default=True)  
    # date = models.DateTimeField(auto_now_add=True , db_index=True )
    # is_deleted = models.BooleanField(default=False, blank=True, null=True) 

    def save(self, *args, **kwargs):
        # Generate a new unique ID if admin_id is not set
        if not self.admin_id:
            self.admin_id = self.generate_unique_id()
        super(Admin, self).save(*args, **kwargs)
    
    def generate_unique_id(self):
        # Generate and return a unique ID
        new_id = uuid.uuid4().hex[:8]
        # Ensure the ID is unique
        while Admin.objects.filter(admin_id=new_id).exists():
            new_id = uuid.uuid4().hex[:8]
        return new_id
    
    def save(self, *args, **kwargs):
        # Agar password plain text ho to usko hash karke save karo
        if self.admin_password and not self.admin_password.startswith('pbkdf2_'):
            self.admin_password = make_password(self.admin_password)
        super(Admin, self).save(*args, **kwargs)    

    

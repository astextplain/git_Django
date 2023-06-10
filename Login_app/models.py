from django.db import models
from django.contrib.auth.models import User
#with this User all field of django admin




# Create your models here.
class UserInfo(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
# This allows you to extend the User model with additional fields by creating a related model, 
# UserInfo, which has a one-to-one relationship with User. 
# By doing this, you can store additional information about the user that is not part of the default User model fields.
    facebook_id =models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    #if you are working with image have to run commad pip install pillow
    def __str__(self):
        return self.user.username
from django.db import models
from userapp.utils import slug_save,upload_image,auto_delete_image_on_change,auto_delete_image_on_delete
from django.db.models.signals import pre_save,post_delete
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image,blank=True,null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_name(self):
        self.user.get_full_name()
    
    def upload_to(self):
        return 'user/'

    
    def __str__(self):
        return str(self.user)


pre_save.connect(slug_save, sender=Profile)
pre_save.connect(auto_delete_image_on_change,sender=Profile)
post_delete.connect(auto_delete_image_on_delete,sender=Profile)
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table ='post'
    name=models.CharField(
        'Name', blank=False, null = False, max_length=14, db_index=True,default='anonymous'
    )
        
    body=models.CharField(
        'body', blank=False, null=False, max_length=140, db_index = True
    )

    created_at =models.DateTimeField(
        'Created DateTime', blank = False, auto_now_add=True
    )
    like_count = models.IntegerField(
        'like_count', blank = True, default = 0, 
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True,
    )

from django.db import models # type: ignore

# Create your models here.

class MyBlog(models.Model):
    image=models.ImageField(upload_to="images/",null=True,blank=True,)
    title=models.CharField(max_length=200,null=True)
    author=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=1200,null=True)
    caption=models.CharField(max_length=200,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
      Category_name = models.CharField(max_length=100,unique=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True) 

      def __str__(self):
            return self.Category_name

class Blogs(models.Model):
      title = models.CharField(max_length=100,unique=True)
      slug = models.SlugField(max_length=100,unique=True,blank=True)
      category=models.ForeignKey(Categorie,on_delete=models.CASCADE)
      author = models.ForeignKey(User,on_delete=models.CASCADE)
      blog_image=models.ImageField(upload_to='uploads/%y/%m/%d')
      short_description=models.CharField(max_length=2000)
      blog_body=models.TextField(max_length=5000)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      



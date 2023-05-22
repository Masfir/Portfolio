from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phonenumber = models.CharField(max_length=15)
    description = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name
    
class Blogs(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    link = models.TextField()
    authname = models.CharField(max_length=30)
    img = models.ImageField(upload_to="blog",blank=True,null=True)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.title

    
    
    
    
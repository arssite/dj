from django.db import models

# Create your models here.
   
class User(models.Model):
    fname = models.CharField(max_length=100,default='DefaultName')
    email=models.EmailField(default="anmol2003@gmail.com")
    address = models.TextField(null=True)
    city = models.CharField(max_length=50, default='Unknown')  # Default value specified here
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    subject = models.TextField(null=True)
    image = models.ImageField(upload_to="img")
    

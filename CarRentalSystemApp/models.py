from django.db import models

# Create your models here.

# Category Model
class Category(models.Model):
    categoryname = models.CharField(max_length=50, blank=False, default='')
    description= models.CharField(max_length=150, blank=False, default='')
    icon=models.ImageField(upload_to='static/')

# Sub Category Model    
class SubCategory(models.Model):
    categoryid = models.CharField(max_length=70, blank=False, default='')
    companyname = models.CharField(max_length=70, blank=False, default='')
    subcategoryname = models.CharField(max_length=70, blank=False, default='')
    subcategorydescription = models.CharField(max_length=150, blank=False, default='')
    subcategoryicon = models.ImageField(upload_to='static/')    


# Vehicle Model 
class Vehicle(models.Model):
    categoryid = models.CharField(max_length=100, blank=False, default='')
    subcategoryid = models.CharField(max_length=100, blank=False, default='')
    modelyear = models.CharField(max_length=170, blank=False, default='')
    variant = models.CharField(max_length=170, blank=False, default='')
    price = models.CharField(max_length=170, blank=False, default='')
    insured = models.CharField(max_length=70, blank=False, default='')
    registrationno = models.CharField(max_length=170, blank=False, default='')
    ownername = models.CharField(max_length=170, blank=False, default='')
    mobileno = models.CharField(max_length=170, blank=False, default='')
    color = models.CharField(max_length=170, blank=False, default='')
    fueltype = models.CharField(max_length=170, blank=False, default='')
    numofseats = models.CharField(max_length=170, blank=False, default='')
    transmissiontype = models.CharField(max_length=170, blank=False, default='')
    vehicleicon = models.ImageField(upload_to='static/')
    
# Admin Model 
class Admin(models.Model):
    adminname = models.CharField(max_length=70, blank=False, default='')
    mobileno= models.CharField(max_length=15, blank=False, default='')
    emailid= models.CharField(max_length=150, blank=False, default='')
    password= models.CharField(max_length=150, blank=False, default='')
    adminpic = models.ImageField(upload_to='static/')  
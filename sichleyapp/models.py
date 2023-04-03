from django.db import models
from django.shortcuts import reverse

class Customer(models.Model):
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    email=models.EmailField(max_length=255)
    

    def __str__(self):
        return self.first_name + ''+ self.last_name
    
    def get_absolute_url(self):
        return reverse('home')
    
class Region(models.Model):
    region_name=models.CharField(max_length=333)
    county_name=models.CharField(max_length=233)
    subcounty_name=models.CharField(max_length=233)
    nearest_Town=models.CharField(max_length=233)

    def __str__(self):
        return self.region_name + ' '+ self.county_name+' ' + self.nearest_Town
    
    def get_absolute_url(self):
        return reverse('region')
    
class land(models.Model):
    land_size=models.CharField(max_length=1500)
    soil_type=models.CharField(max_length=550)
    land_shape=models.CharField(max_length=233)
    land_type=models.CharField(max_length=200)

    
    def __str__(self):
        return self.land_size + '\n'+ self.soil_type +'\n ' + self.land_shape+ ' \n' +self.land_type
    
    def get_absolute_url(self):
        return reverse('land')


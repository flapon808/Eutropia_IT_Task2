from django.db import models

# Create your models here.


#Fashion models start

class T_shirt_Cloths(models.Model):   #Creating a model T-shirt Cloth
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Shirt_Cloths(models.Model):  #Creating a model Shirt Cloths
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Women_Cloths(models.Model):  #Creating a model Women Cloths
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
#Fashion models End



#Electronices models start

class Mobile(models.Model):  #Creating a model for Mobile
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Computer(models.Model):  #Creating a model for Computer
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"

class Laptop(models.Model):  #Creating a model for Laptop
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
#Electronices models end


#Jewellery models start

class Jumkas(models.Model):  #Creating a model for Jumkas 
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Necklaces(models.Model):  #Creating a model for Necklaces
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Kangans(models.Model):  #Creating a model for Kangans
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"

#Jewellery models end
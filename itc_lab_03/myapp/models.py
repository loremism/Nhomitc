from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    Size = models.CharField(max_length=255, blank=True, null=True)
    color= models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Create your models here.
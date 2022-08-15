from django.db import models



class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100)





class Products(models.Model):
    product= models.CharField(max_length=100)



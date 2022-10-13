from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from django.db import models
from PIL import Image
# Create your models here.
CATEGORY = [
    ('Mobiles&Acc','Mobiles Phones & Accessories'),
    ('Computers&Acc','Computers & Accessories'),
    ('KitchenAppliance','Kitchen Appliances'),
]

STORES = [
    ('Melcom','Melcom'),
    ('CampuGhana','CampuGhana'),
    ('Franko','Franko Trading'),
    ('LG','LG'),
    ('Hisense','Hisense'),
    ('Samsung','Samsung'),
    ('Techno','Techno Ghana'),
    ('Goodluck','GoodLuck Africa'),
]


class Melcom(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True, unique=True)
    productName = models.CharField(max_length=120, blank=False, null=False)
    productCat = models.CharField(max_length=120, blank=False, null=False, choices=CATEGORY,)
    productPrice = models.CharField(blank=False, null=False, max_length=6)
    productDespription = models.CharField(max_length=120, blank=True, null=True, )
    productImage = models.ImageField(default = 'default.jpg', upload_to = 'melcom/')
    productStore = models.CharField(max_length=120, blank=True, null=True, choices=STORES,)
    productWebAddress = models.URLField(blank=False, null=False)
    dateadded = models.DateField(blank=False, null=False, auto_now=True)
    
    def save(self):
        super().save()  # saving image first
        productImage = Image.open(self.productImage.path) # Open image using self
        if productImage.height > 300 or productImage.width > 300:
            new_img = (470, 270)
            productImage.thumbnail(new_img)
            productImage.save(self.productImage.path)  # saving image at the same path
            
    def __str__(self):
        return self.productName
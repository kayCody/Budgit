from email.mime import image
from pickle import FALSE
from django.db import models
from PIL import Image

# Create your models here.
class Addproducts(models.Model):
    Productsid = models.IntegerField(primary_key=True, blank=False, null=False)
    productName = models.CharField(max_length = 50, null= False)
    description = models.CharField(max_length=200, null=False)
    price = models.CharField(max_length=6, null=False)
    date = models.DateField(blank=False, auto_now=True, null=False)
    image = models.ImageField(default='default.jpg', upload_to = 'proimg/' )
    
    def save(self):
        super().save()  # saving image first
        image = Image.open(self.image.path) # Open image using self
        if image.height > 300 or image.width > 300:
            new_img = (470, 270)
            image.thumbnail(new_img)
            image.save(self.image.path)  # saving image at the same path
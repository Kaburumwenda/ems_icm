from django.db import models
from io import BytesIO
# from PIL import Image

from django.core.files import File

# Create your models here.
class menuEntries(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    page = models.CharField(max_length=255)
    isOpen = models.BooleanField(default=False)
    level = models.CharField(max_length=255, default=0)
    def __str__(self):
        return self.title


class submenu(models.Model):
    title = models.CharField(max_length=255)
    page = models.CharField(max_length=255)
    menuentries = models.ForeignKey(menuEntries, related_name='submenu', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'



class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
        )
    title = models.CharField(max_length=150)
    Bprice = models.DecimalField(max_digits=12, decimal_places=2, default='0.00')
    Sprice = models.DecimalField(max_digits=12, decimal_places=2, default='0.00')
    offer = models.CharField(max_length=30, choices=STATUS, default=False)
    image = models.ImageField(upload_to='products/images')
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2,default='1')
    date = models.DateField(auto_now_add=True, blank = True)

    def __str__(self):
        return f"{self.title}"

    class Meta:  
        db_table = "product"

    def get_absolute_url(self):
        return f'/{self.category.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         return 'http://127.0.0.1:8000' + self.thumbnail.url
    #     else:
    #         if self.image:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()

    #             return 'http://127.0.0.1:8000' + self.thumbnail.url
    #         else:
    #             return ''
    
    # def make_thumbnail(self, image, size=(200, 100)):
    #     img = Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size)

    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)

    #     thumbnail = File(thumb_io, name=image.name)

    #     return thumbnail      



class Fakedata(models.Model):
    cdatetime=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    beat=models.CharField(max_length=255)
    grid=models.CharField(max_length=255)
    crimedescr=models.CharField(max_length=255)
    ucr_ncic_code=models.CharField(max_length=255)
    latitude=models.CharField(max_length=255)
    longitude=models.CharField(max_length=255)

    def __str__(self):
        return self.latitude



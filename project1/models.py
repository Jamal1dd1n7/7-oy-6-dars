from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
# ------------------------------------------------------------------------------------------------------------------------
from PIL import Image

# MyUser model:
class MyUser(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)
    adress = models.TextField(max_length=150, null=True, blank=True)
    photo = models.ImageField(upload_to='users/photo', null=True, blank=True)

    class Meta:
        verbose_name = "Foydalanuvchi "
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ['id'] 

# Department model:
class Department(models.Model):
    # Slug model:
    slug = models.SlugField(max_length=150, unique=True)
    # Title model: 
    name = models.CharField(max_length=255)

        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Turkum"
        verbose_name_plural = "Turkumlar"
        ordering = ['-id']

# ------------------------------------------------------------------------------------------------------------------------

# Category model:
class Category(models.Model):
    # Slug model: Kategoriya slug ni kiritish model;
    slug = models.SlugField(max_length=150, unique=True)
    # Name model: Kategoriya nomini kiritish uchun model. Maksimal uzunligi 255 ta simvol;
    name = models.CharField(max_length=255)
    # Department model: Kategoriyani turkumga ulash uchun model;
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['-id']
# ------------------------------------------------------------------------------------------------------------------------

# Product model:
class Product(models.Model):
    # Slug model: Mahsulot slug ni kiritish uchun model;
    slug = models.SlugField(max_length=150, unique=True)
    # Category model: Kategoriyaga ulash uchun model;
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    # Name model: Mahsulot nomini kiritish uchun model. Maksimal 255 ta simvol kiritish mumkin ;
    name = models.CharField(max_length=255)
    # Description model: Mahsulot haqida ma`lumot kiritish uchun model. Simvol yozishda cheklov yo`q;
    description = models.CharField(max_length=255, null=True, blank=True)
    # Price model: Mahsulot narxini kiritish uchun model;
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Quantity model: Mahsulot miqdorini kiritish uchun model;
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ['-id']
# ------------------------------------------------------------------------------------------------------------------------

# Product Image model:
class ProductImage(models.Model):
    # Image model: ...;
    photo = models.ImageField(upload_to='products/photo')
    # Product model: ...;
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo.name

# ------------------------------------------------------------------------------------------------------------------------

# Comment model:  
class Comment(models.Model):
    # Text model: Dars uchun o`quvchi tomonidan qo`yilishi uchun izoh matnini kiritish uchun model;
    text = models.TextField(max_length=1000)
    # Author: Izoh qoldirgan o`qituvchi yoki o`quvchini avtomatik tarzda kirituvchi uchun model;
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    # Lesson model: Izoh qaysi darsga qoldirilganligini avtomatik tarzda kirituvchi model;
    lesson = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Created model: Izoh qachon qoldirilganligini avtomatik tarzda kirituvchi model;
    created = models.DateTimeField(auto_now_add=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Izoh "
        verbose_name_plural = "Izohlar"
        ordering = ['-id']
# ------------------------------------------------------------------------------------------------------------------------































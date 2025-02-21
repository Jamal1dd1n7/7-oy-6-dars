import random
# Imports:
# Messages: template ga xabar jo`natish uchun ishlatiladi
# ( message.success(request, 'Amal muvaffaqiyatli amalga oshirildi'));
from django.contrib import messages
#--------------------------------------------------------------------------------

# Login, Logout, Authenticate: ...;
from django.contrib.auth import login, logout, authenticate
#--------------------------------------------------------------------------------

# Permission required, login required: Foydalanuvchi uchun ruxsatlar borligini tekshiruvchi funksiyalar;
from django.contrib.auth.decorators import permission_required, login_required
#--------------------------------------------------------------------------------

# Mixin class: Ro`yxatdan o`tganlikka tekshiruvchi class;
from django.contrib.auth.mixins import LoginRequiredMixin
#--------------------------------------------------------------------------------

# Send mail: Xabarni kiritilgan emailga jo`natish uchun ishlatiladi;
from django.core.mail import send_mail
#--------------------------------------------------------------------------------

# Paginator: template da model cheklanganidan ortib ketsa, yangi page da chiqaradigan class;
from django.core.paginator import Paginator
#--------------------------------------------------------------------------------

# WSGIRequest: ...;
from django.core.handlers.wsgi import WSGIRequest
#--------------------------------------------------------------------------------

# Render, Redirect, Get_object_or_404, Get_list_or_404: ...; 
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
#--------------------------------------------------------------------------------

# Reverse lazy: ...;
from django.urls import reverse_lazy
#--------------------------------------------------------------------------------

# View class: ...;
from django.views import View
#--------------------------------------------------------------------------------

# Generic Views: Oldindan tayyorlangan "view"lar( ListView, DetailView);
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#--------------------------------------------------------------------------------

# Generic Views: Oldindan tayyorlangan "view"lar( Login, Register, Logout);
from django.contrib.auth.views import LoginView, LogoutView

# Now function: Ayni vaqtni olib beruvchi funksiya;
from django.utils.timezone import now 
#--------------------------------------------------------------------------------

# Datetime function: Bugungi sana, oy, yilni olib beruvchi funksiya;
from datetime import datetime
#--------------------------------------------------------------------------------

# User model: User uchun yozilgan model;
# from django.contrib.auth.models import User
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# .models: models.py faylidan modellarni import qiladi;
from .models import *
#--------------------------------------------------------------------------------

# .forms: forms.py faylidan formlarni import qiladi; 
from .forms import *

# Generic Views
# Views:
# Home,
# Auth(Login, Logout),
# Message(send_message)

# Home


# HomeView - Asosiy sahifa uchun tasodifiy mahsulotlar chiqarish
class HomeView(ListView):
    model = Product
    template_name = 'project1/detail_templates/intex.html'
    context_object_name = "products"
    paginate_by = 10

    extra_context = {
        "title": "Home"
    }

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Products
class ProductsView(ListView):
    template_name = 'project1/products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            return Product.objects.filter(category_id=category_id)  
        return Product.objects.all()  
    extra_context = {
        "title": "Products"
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  
        return context
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    
# Product detail  
class ProductDetail(DetailView):
    model = Product
    template_name = 'project1/detail_templates/product.html'
    context_object_name = 'product'

    def get_object(self):
        product_slug = self.kwargs.get('product_slug')
        return get_object_or_404(Product, slug=product_slug)
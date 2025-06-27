from django.contrib import admin

# Register your models here.

from .models import Myapp_Model

admin.site.register(Myapp_Model)
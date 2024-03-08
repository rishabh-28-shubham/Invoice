from django.contrib import admin

# from .models import *
# importing every model seperatly 
from .models import Client, Product, Invoice, Settings


# Register your models here.

admin.site.register(Client)

#Register Settings, Product and Invoice Models
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Settings)
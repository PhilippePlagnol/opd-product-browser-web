from django.contrib import admin

# Register your models here.
from .models import Brand, Gtin

admin.site.register(Brand)
admin.site.register(Gtin)

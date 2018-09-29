from django.contrib import admin
from .models import Picture, Location, Category

# Register your models here.
admin.site.register(Picture)
admin.site.register(Location)
admin.site.register(Category)
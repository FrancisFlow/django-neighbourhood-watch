from django.contrib import admin
from .models import Business, Profile, NeighbourHood

# Register your models here.
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(NeighbourHood)

from django.contrib import admin

from petstragram.main_app.models import Pet, Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin

# Register your models here.
from .models import ClothingBrand, LocalEvent, Recipe, FoodCentre, Other, UpcomingMegaSale

admin.site.register(ClothingBrand)
admin.site.register(LocalEvent)
admin.site.register(Recipe)
admin.site.register(FoodCentre)
admin.site.register(Other)
admin.site.register(UpcomingMegaSale)
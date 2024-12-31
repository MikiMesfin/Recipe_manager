from django.contrib import admin
from .models import Category, Recipe, Rating, Favorite, MealPlan, ShoppingList, NutritionalInfo

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(MealPlan)
admin.site.register(ShoppingList)
admin.site.register(NutritionalInfo)

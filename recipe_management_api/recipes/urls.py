from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'meal-plans', views.MealPlanViewSet, basename='mealplan')
router.register(r'shopping-lists', views.ShoppingListViewSet, basename='shoppinglist')

urlpatterns = [
    path('', include(router.urls)),
] 
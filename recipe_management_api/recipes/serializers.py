from rest_framework import serializers
from .models import Recipe, Category, Rating, Favorite, MealPlan, ShoppingList, NutritionalInfo
from django.conf import settings
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    average_rating = serializers.SerializerMethodField()
    nutritional_info = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('created_date', 'updated_date', 'creator', 'nutritional_info')

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings:
            return sum(rating.value for rating in ratings) / len(ratings)
        return None

    def get_nutritional_info(self, obj):
        if hasattr(obj, 'nutritional_info'):
            return {
                'calories': obj.nutritional_info.calories,
                'protein': obj.nutritional_info.protein,
                'carbohydrates': obj.nutritional_info.carbohydrates,
                'fat': obj.nutritional_info.fat,
                'fiber': obj.nutritional_info.fiber
            }
        return None

class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ('user', 'recipe')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        read_only_fields = ('user', 'recipe')

class MealPlanSerializer(serializers.ModelSerializer):
    recipe_detail = RecipeSerializer(source='recipe', read_only=True)

    class Meta:
        model = MealPlan
        fields = '__all__'
        read_only_fields = ('user',)

class ShoppingListSerializer(serializers.ModelSerializer):
    ingredients_list = serializers.SerializerMethodField()
    recipes_detail = RecipeSerializer(source='recipes', many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = '__all__'
        read_only_fields = ('user',)

    def get_ingredients_list(self, obj):
        ingredients = {}
        for recipe in obj.recipes.all():
            for ingredient in recipe.ingredients:
                if ingredient['item'] in ingredients:
                    ingredients[ingredient['item']]['quantity'] += ingredient['quantity']
                else:
                    ingredients[ingredient['item']] = {
                        'quantity': ingredient['quantity'],
                        'unit': ingredient['unit']
                    }
        return ingredients

class NutritionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalInfo
        fields = '__all__'
        read_only_fields = ('recipe',)
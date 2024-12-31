from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Recipe, Category, Rating, Favorite

User = get_user_model()

class RecipeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        
        self.category = Category.objects.create(
            name='Test Category',
            description='Test Description'
        )
        
        self.recipe_data = {
            'title': 'Test Recipe',
            'description': 'Test Description',
            'ingredients': [{'item': 'test ingredient', 'quantity': 1, 'unit': 'cup'}],
            'instructions': 'Test Instructions',
            'category': self.category.id,
            'preparation_time': 30,
            'cooking_time': 30,
            'servings': 4
        }

    def test_create_recipe(self):
        url = reverse('recipe-list')
        response = self.client.post(url, self.recipe_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Recipe.objects.get().title, 'Test Recipe')

    def test_list_recipes(self):
        recipe_data = self.recipe_data.copy()
        recipe_data.pop('category')  # Remove category from dict to avoid duplicate
        Recipe.objects.create(
            creator=self.user,
            category=self.category,
            **recipe_data
        )
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    def test_rate_recipe(self):
        recipe_data = self.recipe_data.copy()
        recipe_data.pop('category')
        recipe = Recipe.objects.create(
            creator=self.user,
            category=self.category,
            **recipe_data
        )
        url = reverse('recipe-rate', kwargs={'pk': recipe.pk})
        response = self.client.post(url, {'value': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rating.objects.count(), 1)
        self.assertEqual(Rating.objects.get().value, 5)

    def test_favorite_recipe(self):
        recipe_data = self.recipe_data.copy()
        recipe_data.pop('category')
        recipe = Recipe.objects.create(
            creator=self.user,
            category=self.category,
            **recipe_data
        )
        url = reverse('recipe-favorite', kwargs={'pk': recipe.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Favorite.objects.count(), 1)


class UserTests(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'bio': 'Test bio'
        }
        
    def test_create_user(self):
        url = reverse('user-create')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_user_login(self):
        User.objects.create_user(**self.user_data)
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_detail(self):
        user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=user)
        url = reverse('user-detail', kwargs={'pk': user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user_data['username'])
    def test_user_update(self):
        user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=user)
        url = reverse('user-detail', kwargs={'pk': user.pk})
        update_data = {'bio': 'Updated bio'}
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=user.pk).bio, 'Updated bio')

    def test_unauthorized_access(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
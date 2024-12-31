# Recipe Management API

A Django REST API for managing recipes, meal plans, and shopping lists.

## Features
- User authentication with JWT
- Recipe CRUD operations
- Category management
- Meal planning
- Shopping list generation
- Recipe ratings and favorites
- Nutritional information tracking

## Tech Stack
- Django 4.2+
- Django REST Framework
- SimpleJWT for authentication
- SQLite (development)
- Pillow for image handling

## Setup
1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create .env file and set variables:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Run development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- POST `/api/token/` - Obtain JWT token
- POST `/api/token/refresh/` - Refresh JWT token

### Users
- POST `/api/users/create/` - Register new user
- GET `/api/users/` - List users (authenticated)
- GET `/api/users/{id}/` - Get user details
- PUT `/api/users/{id}/` - Update user
- DELETE `/api/users/{id}/` - Delete user

### Recipes
- GET `/api/recipes/recipes/` - List recipes
- POST `/api/recipes/recipes/` - Create recipe
- GET `/api/recipes/recipes/{id}/` - Get recipe details
- PUT `/api/recipes/recipes/{id}/` - Update recipe
- DELETE `/api/recipes/recipes/{id}/` - Delete recipe
- POST `/api/recipes/recipes/{id}/rate/` - Rate recipe
- POST `/api/recipes/recipes/{id}/favorite/` - Favorite recipe

### Categories
- GET `/api/recipes/categories/` - List categories
- POST `/api/recipes/categories/` - Create category

### Meal Plans
- GET `/api/recipes/meal-plans/` - List meal plans
- POST `/api/recipes/meal-plans/` - Create meal plan

### Shopping Lists
- GET `/api/recipes/shopping-lists/` - List shopping lists
- POST `/api/recipes/shopping-lists/` - Create shopping list

## Testing
Run tests with:
```bash
python manage.py test
```
## License
[Add your chosen license]
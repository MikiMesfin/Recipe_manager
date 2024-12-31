from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('', views.UserListView.as_view(), name='user-list'),
] 
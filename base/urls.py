from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),

    path('activity/', views.activityPage, name='activity'),
    path('topics/', views.topicsPage, name='topics'),

    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('update-user/<str:pk>/', views.updateUser, name='update-user'),

    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
]

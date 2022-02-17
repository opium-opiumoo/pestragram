from django.urls import path
from petstragram.main_app.views import create_pet, create_pet_photo, create_profile, delete_pet, delete_profile, edit_pet, edit_pet_photo, edit_profile, like_pet, show_home, show_dashboard, show_profile, show_pet_photo_details

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet ,name='like pet photo'),
    path('photo/add/', create_pet_photo ,name='add pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo ,name='edit pet photo'),
    
    path('pet/create', create_pet, name='create pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),
)
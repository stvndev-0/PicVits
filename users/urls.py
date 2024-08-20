from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('<str:username>/', views.profile_view, name='profile'),
    path('profile/update_profile/', views.update_profile_view, name='update_profile'),
    path('profile/change_image/', views.change_image_view, name='change_image'),
    path('profile/update_password/', views.update_password_view, name='update_password'),
]
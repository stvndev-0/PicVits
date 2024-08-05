from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('new_picture/', views.new_picture_view, name='new_picture'),
    path('update_picture/<int:pict_id>/edit/', views.update_picture_view, name='update_picture'),
    path('pict/<int:pict_id>/', views.pict_view, name='pict'),
    path('search/', views.search_view, name='search'),
]
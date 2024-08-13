from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('new_picture/', views.new_picture_view, name='new_picture'),
    path('pict/<int:pict_id>/', views.pict_view, name='pict'),
    path('pict/<int:pict_id>/comment/', views.add_comment_view, name='add_comment'),
    # path('pict/<int:pict_id>/comment/<int:>/', views.add_comment_view, name='add_comment_reply'),
    path('pict/<int:pict_id>/comment/delete_comment/<int:comment_id>', views.delete_comment_view, name='delete_comment'),
    path('pict/<int:pict_id>/edit/', views.update_picture_view, name='update_picture'),
    path('pict/<int:pict_id>/delete/', views.delete_picture_view, name='delete_picture'),
    path('search/', views.search_view, name='search'),
]
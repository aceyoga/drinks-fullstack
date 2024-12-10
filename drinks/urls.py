from django.urls import path
from .views import index, get_all_drinks, get_drink, create_drink, update_drink, delete_drink

urlpatterns = [
    path('', index, name='index'),
    path('api/drinks/', get_all_drinks, name='get_all_drinks'),
    path('api/drinks/<int:drink_id>/', get_drink, name='get_drink'),
    path('api/drinks/create/', create_drink, name='create_drink'),
    path('api/drinks/update/<int:drink_id>/', update_drink, name='update_drink'),
    path('api/drinks/delete/<int:drink_id>/', delete_drink, name='delete_drink'),
]
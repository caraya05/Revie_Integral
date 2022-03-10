from django.urls import path

from reviews.views.restaurant_view import RestaurantView

app_name = 'reviews'

urlpatterns = [
    path('', RestaurantView.as_view(), name='restaurant_list'),
]

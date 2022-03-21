from django.urls import path

from reviews.views.restaurant_view import RestaurantView, TopView
from reviews.views.register_view import RegisterReviewerView

app_name = 'reviews'

urlpatterns = [
    path('restaurant-list/', RestaurantView.as_view(), name='restaurant_list'),
    path('restaurant-top/', TopView.as_view(), name='restaurant_top'),
    path('register-reviewer/', RegisterReviewerView.as_view(), name='register_reviewer'),
]

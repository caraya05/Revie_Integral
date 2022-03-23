from django.urls import path

from reviews.views.restaurant_view import RestaurantView, TopView, RestaurantDetailView, ReviewerDetailView
from reviews.views.register_view import RegisterReviewerView, UpdateReviewerView, RegisterReviewView

app_name = 'reviews'

urlpatterns = [
    path('restaurant-list/', RestaurantView.as_view(), name='restaurant_list'),
    path('restaurant-top/', TopView.as_view(), name='restaurant_top'),
    path('update-reviewer/<int:pk>/', UpdateReviewerView.as_view(), name='update_reviewer'),
    path('register-reviewer/', RegisterReviewerView.as_view(), name='register_reviewer'),
    path('review_r/', RegisterReviewView.as_view(), name='review'),
    path('restaurant/<uuid:pk>/', RestaurantDetailView.as_view(), name='restaurant'),
    path('reviewer/<int:pk>/', ReviewerDetailView.as_view(), name='reviewer'),
]

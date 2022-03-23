from django.views.generic import ListView, TemplateView, DetailView

from reviews.models import Restaurant, photo_restaurant, PhotoRestaurant, Review, PhotoReview
from users.models import Person


class RestaurantView(ListView):
    model = Restaurant
    template_name = "restaurant.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TopView(TemplateView):
    # login_url = "/login"
    template_name = "top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurants'] = Restaurant.objects.order_by('-score')[:3]
        return context


class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = "profile_restaurant.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant_images = PhotoRestaurant.objects.filter(restaurant__id=self.object.id)
        context['restaurant_images'] = restaurant_images
        reviews_res = Review.objects.filter(place__id=self.object.id)
        context['reviews_res'] = reviews_res
        return context

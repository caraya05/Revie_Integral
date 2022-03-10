from django.views.generic import ListView

from reviews.models import Restaurant


class RestaurantView(ListView):
    model = Restaurant
    # login_url = "/login"
    template_name = "restaurant.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

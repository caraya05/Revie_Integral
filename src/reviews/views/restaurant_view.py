from django.views.generic import ListView, TemplateView

from reviews.models import Restaurant


class RestaurantView(ListView):
    model = Restaurant
    # login_url = "/login"
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

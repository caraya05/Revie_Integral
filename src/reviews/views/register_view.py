from django.views.generic import CreateView

from reviews.models import Reviewer


class RegisterReviewer(CreateView):
    model = Reviewer
    # login_url = "/login"
    template_name = "register_reviewer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

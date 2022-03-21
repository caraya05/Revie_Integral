from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from reviews.forms.reviewer_fom import ReviewerForm
from users.models import Person


class RegisterReviewerView(CreateView):
    model = Person
    form_class = ReviewerForm
    template_name = "register_reviewer.html"
    success_url = reverse_lazy('login')
    print("pinche formulario")

    def form_valid(self, form):
        print("selffff",)
        print("formmmm",)
        form.save()  # pylint: disable=W0707 W0201
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=email, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('login'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_authenticate'] = str(self.request.user)
        return context


import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from reviews.forms.review_form import ReviewForm
from reviews.forms.reviewer_fom import ReviewerForm
from reviews.forms.updatereviewer_fom import UpdateReviewerForm
from reviews.models import Review, Restaurant
from users.models import Person


class RegisterReviewerView(CreateView):
    model = Person
    form_class = ReviewerForm
    template_name = "register_reviewer.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
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


class RegisterReviewView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Review
    form_class = ReviewForm
    template_name = "review.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)  # pylint: disable=W0707 W0201
        self.object.person = self.request.user
        place = self.request.GET.get('restaurant')
        self.object.place = Restaurant.objects.filter(id=place).first()
        self.object.save()
        print('aca si esta', self.request.user.id)
        return HttpResponseRedirect(
            reverse('reviews:restaurant', args=[Restaurant.objects.filter(id=place).first().id]))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class UpdateReviewerView(UpdateView):
    model = Person
    form_class = UpdateReviewerForm
    template_name = "update_reviewer.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_authenticate'] = str(self.request.user)
        return context

import random
import string

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from commons.forms.login_form import LoginModelForm
from commons.helpers.utils import send_mail_forgot
from users.models import Person


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutUsView(TemplateView):
    template_name = "about-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MapSiteView(TemplateView):
    template_name = "map_site.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginModelForm

    def form_valid(self, form):
        user = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(username=user, password=password)
        if not user:
            messages.error(self.request, _("Usuario o contraseña invalidos"))
            return HttpResponseRedirect(reverse_lazy('login'))
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('index'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Logout(LogoutView):
    template_name = 'login.html'


def forgot_password(request):
    validate_email = request.GET.get('email')
    user = Person.objects.filter(email=validate_email).first()
    subject = _("Recovery password")
    if user:
        if user.email:
            ran = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            user.set_password(ran)
            user.save()
            message = render_to_string("emails/forgot.html", context={
                'get_full_name': user.get_full_name(),
                'profile': user.email,
                'password': ran
            }).strip()
            send_mail_forgot(user.email, message, subject)
            messages.success(request,
                             _("Email validate, has been sent to the mail the new password."))
            return HttpResponseRedirect(reverse_lazy('index'))
    messages.success(request, _("Email validate, has been sent to the mail the new password."))
    return HttpResponseRedirect(reverse_lazy('persons:persons-forgotView'))

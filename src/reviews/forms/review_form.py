from django.forms import NumberInput
from django.utils.translation import ugettext_lazy as _

from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    photo_one = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-sm',
                                                               'accept': 'image/jpg, image/jpeg, image/png'}))
    photo_two = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-sm',
                                                               'accept': 'image/jpg, image/jpeg, image/png'}))
    photo_three = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-sm',
                                                                 'accept': 'image/jpg, image/jpeg, image/png'}))

    title = forms.CharField(label=_('Title'),
                            widget=forms.TextInput(attrs={
                                'class': 'form-control form-control-sm input_register',
                                'placeholder': _('Title')}))
    description = forms.CharField(label=_("Description"), widget=forms.Textarea(
        attrs={'placeholder': _('Enter your description'), 'rows': 5, 'cols': 20,
               'class': 'form-control form-control-sm input_register'}))

    score_service = forms.IntegerField(
        widget=NumberInput(attrs={'class': 'form-range  slider', 'type': 'range', 'step': '1', 'min': '0', 'max': '5'}))
    score_food = forms.IntegerField(
        widget=NumberInput(attrs={'class': 'form-range  slider', 'type': 'range', 'step': '1', 'min': '0', 'max': '5'}))
    score_environment = forms.IntegerField(
        widget=NumberInput(attrs={'class': 'form-range  slider', 'type': 'range', 'step': '1', 'min': '0', 'max': '5'}))
    score_quality_price = forms.IntegerField(
        widget=NumberInput(attrs={'class': 'form-range  slider', 'type': 'range', 'step': '1', 'min': '0', 'max': '5'}))

    class Meta:
        model = Review

        fields = [
            'title',
            'description',
            'score_service',
            'score_food',
            'score_environment',
            'score_quality_price',
            'photo_one',
            'photo_two',
            'photo_three',
        ]

from django import forms
from .models import Place
from django.utils.translation import gettext_lazy as _
from functools import partial


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
        labels = {
            'title': _('제목'),
            'description':_('한줄 소개'),
            'image': _('사진'),
        }
        widgets = {
            'state': forms.HiddenInput(),
            'light': forms.HiddenInput(),
            'PIR': forms.HiddenInput(),
        }
        help_texts = {

        }


class UpdatePlaceForm(PlaceForm):
    class Meta:
        model = Place
        exclude = ()

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(PlaceForm, self).__init__(*args, **kwargs)
    #
    # def save(self, commit=True):
    #     instance = super(PlaceForm, self).save(commit=False)
    #
    #     if commit:
    #         instance.save()
    #     return instance
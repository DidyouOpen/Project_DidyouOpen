from django import forms
from .models import Reservation
from django.utils.translation import gettext_lazy as _


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['place', 'comment', 'user', 'created_at']
        labels = {
            'place':_('장'),
            'comment': _('코멘'),
            'created_at': _('예약날짜 및 시간'),
        }
        widgets = {
            'user': forms.HiddenInput(),
        }
        help_texts = {

        }


class UpdateHistoryForm(ReservationForm):
    class Meta:
        model = Reservation

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ReservationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ReservationForm, self).save(commit=False)

        if commit:
            instance.save()
        return instance
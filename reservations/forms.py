from django import forms
from .models import Reservation
from django.contrib.admin import widgets
from django.utils.translation import gettext_lazy as _
from django import forms
from functools import partial
from datetimepicker.widgets import DateTimePicker

DateInput = partial(forms.DateTimeInput, {'class': 'datepicker'})

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['place', 'comment', 'user', 'created_at']
        labels = {
            'place':_('장소'),
            'comment': _('코멘트'),
            'created_at': _('예약날짜 및 시간'),
        }
        widgets = {
            'user': forms.HiddenInput(),
            'created_at' : DateInput(),
        }
        help_texts = {

        }


class UpdateReservationForm(ReservationForm):
    class Meta:
        model = Reservation
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ReservationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ReservationForm, self).save(commit=False)

        if commit:
            instance.save()
        return instance
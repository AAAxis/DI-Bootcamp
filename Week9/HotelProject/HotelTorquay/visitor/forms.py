from django.db import models
from django import forms
from functools import partial
from .models import Booking
from .widgets import DatePickerInput


DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class BookingForm(forms.Form):
    check_in = forms.DateField(widget=DatePickerInput)
    check_out = forms.DateField(widget=DatePickerInput)
        
        
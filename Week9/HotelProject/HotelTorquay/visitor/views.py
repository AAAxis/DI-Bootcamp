from django.shortcuts import render, redirect
from django.views import generic
from django import forms
from .forms import BookingForm
from .models import Booking


def index(request):
    context = {'form':BookingForm}

    if request.method == 'POST':
        form_filled = BookingForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('index')
        else:
            print(form_filled.errors)
    return render(request, 'index.html', context)    
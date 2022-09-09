from tkinter import CASCADE
from django.db import models


class Booking(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
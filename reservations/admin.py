from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation



admin.site.register(Reservation, ReservationAdmin)
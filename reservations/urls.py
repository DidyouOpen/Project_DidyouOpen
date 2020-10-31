from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('reservation/', views.reservation, name='reservation-list'),
    path('reservation/update/',views.reservation_update,name='reservation-update'),
    path('reservation/create/',views.reservation_create,name='reservation-create'),
]
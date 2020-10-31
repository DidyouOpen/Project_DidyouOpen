from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('place/', views.place, name='place-list'),
    path('place/update/',views.place_update,name='place-update'),
    path('place/create/',views.place_create,name='place-create'),
]
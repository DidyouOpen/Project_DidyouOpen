from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('reservation/', views.reservation, name='reservation-list'),
    path('reservation/update/',views.reservation_update,name='reservation-update'),
    # path('reservation/create/<int:place_id>/',views.reservation_create,name='reservation-create'),
    path('reservation/<int:id>/delete/', views.reservation_delete,name='reservation-delete'),
]
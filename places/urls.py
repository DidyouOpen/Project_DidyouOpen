from django.urls import path
from django.conf.urls import url
from . import views
from . import viewsets
from django.views.generic import TemplateView

urlpatterns = [
    path('place/', views.place, name='place-list'),
    path('',views.home,name='home'),
    path('about/', TemplateView.as_view(template_name='intro.html'), name='about'),
    path('place/update/',views.place_update,name='place-update'),
    path('place/create/',views.place_create,name='place-create'),
    path('place/stores/', viewsets.Valueview.as_view(), name="place-stores"),
    # path('places/stores/', TemplateView.as_view(template_name="place_stores.html"), name='place_stores'),
]
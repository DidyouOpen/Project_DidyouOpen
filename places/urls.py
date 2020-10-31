from django.urls import path
from django.conf.urls import url
from . import views
from . import viewsets
urlpatterns = [
    url('value', viewsets.Valueview.as_view(), name="value")

]
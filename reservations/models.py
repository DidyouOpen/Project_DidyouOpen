from django.db import models
# from accounts.models import User
from places.models import Place


class Reservation(models.Model):
    comment = models.TextField(max_length=1000, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
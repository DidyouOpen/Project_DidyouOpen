from django.db import models

class Place(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="blog/%Y/%m/%d")
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    latitude = models.FloatField(default=0, null=True)
    longitude = models.FloatField(default=0, null=True)
    light = models.FloatField(default=0, null=True)
    PIR = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title
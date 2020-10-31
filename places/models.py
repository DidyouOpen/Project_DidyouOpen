from django.db import models

STATUS_CHOICES = (
    (0, '불은 켜져 있지만 사람은 없음'),
    (1, '불도 켜져 있고 사람도 있음'),
    (2, '불은 꺼져 있지만 사람이 있음'),
    (3, '불도 꺼져 있고 사람도 없음'),
    (4, '화재 의심'),
    (5, '센서 작동 불분명'),
)

class Place(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="blog/%Y/%m/%d")
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    # latitude = models.FloatField(default=0, null=True)
    # longitude = models.FloatField(default=0, null=True)
    state = models.IntegerField(blank=True, choices=STATUS_CHOICES, default=3)

    def __str__(self):
        return self.title
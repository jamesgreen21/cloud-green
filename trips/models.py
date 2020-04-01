from django.db import models
from django.utils import timezone


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Trip(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    star = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('trips:detail', args=[str(self.id)])

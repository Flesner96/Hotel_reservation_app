from django.db import models
from datetime import date

# Create your models here.
class Sala(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    projector_availability = models.BooleanField(default=False)

    def is_booked_today(self):
        return self.rezerwacja_set.filter(data=date.today()).exists()


class Rezerwacja(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data = models.DateField()
    komentarz = models.TextField()

    class Meta:
        unique_together = ('sala', 'data',)
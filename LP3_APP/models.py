from django.db import models

# Create your models here.


class Region(models.Model):
    idregion = models.AutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='region_images/')
    cases = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    lethality = models.FloatField()

    def __str__(self):
        return self.name

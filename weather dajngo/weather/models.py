from django.db import models

# Create your models here.



class City(models.Model):
    name = models.CharField(max_length=255)
    coord_lon = models.FloatField()
    coord_lat = models.FloatField()

    def __str__(self):
        return '{}-{}'.format(self.id,self.name)


class Weath(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    temp = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    wind_deg = models.IntegerField()
    date = models.DateField(auto_now=True)



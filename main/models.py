from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    


class Fuel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class FuelStation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to='station/', blank=True, null=True)
    avaliable_fuels = models.ManyToManyField(Fuel, blank=True)
    closing_time = models.TimeField()
    opening_time = models.TimeField()
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name
    
    @property
    def price(self):
        return Price.objects.filter(station=self).first()
    


class Price(models.Model):
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    price = models.FloatField()
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.station.name} - {self.fuel.name} - {self.price}'


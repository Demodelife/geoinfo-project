from django.db import models


class GeoName(models.Model):
    """
    Model GeoName.
    """
    geonameid = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    asciiname = models.CharField(max_length=200, null=False, blank=False)
    alternatenames = models.CharField(max_length=10000, null=False, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=False, blank=False)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=False, blank=False)
    feature_class = models.CharField(max_length=1, null=False, blank=True)
    feature_code = models.CharField(max_length=10, null=False, blank=True)
    country_code = models.CharField(max_length=2, null=False, blank=True)
    cc2 = models.CharField(max_length=200, null=False, blank=True)
    admin1_code = models.CharField(max_length=20, null=False, blank=True)
    admin2_code = models.CharField(max_length=80, null=False, blank=True)
    admin3_code = models.CharField(max_length=20, null=False, blank=True)
    admin4_code = models.CharField(max_length=20, null=False, blank=True)
    population = models.BigIntegerField(default=0, null=False, blank=True)
    elevation = models.IntegerField(default=0, null=False, blank=True)
    dem = models.IntegerField(default=0, null=False, blank=True)
    timezone = models.CharField(max_length=40, null=False, blank=True)
    modification_date = models.DateField(null=False, blank=True)

    def __str__(self):
        return f'GeoName "{self.geonameid}"'

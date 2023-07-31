from rest_framework import serializers
from geoinfo_apiapp.models import GeoName


class GeoNameSerializer(serializers.ModelSerializer):
    """
    GeoName Serializer Class.
    To serialize information across objects.
    """
    class Meta:
        model = GeoName
        fields = '__all__'

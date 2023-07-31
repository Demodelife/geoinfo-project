from django.contrib import admin

from geoinfo_apiapp.models import GeoName


@admin.register(GeoName)
class GeoNameAdmin(admin.ModelAdmin):
    list_display = (
        'geonameid',
        'name',
        'alternatenames',
        'latitude',
        'longitude',
        'timezone',
    )
    list_display_links = 'geonameid',
    search_fields = 'geonameid', 'name', 'alternatenames'

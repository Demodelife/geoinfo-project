from django.urls import path
from geoinfo_apiapp.views import GeoNameRetrieveAPIView, GeoNameListAPIView

app_name = 'geoinfo_apiapp'

urlpatterns = [
    path('geoinfo/', GeoNameListAPIView.as_view(), name='geo-list'),
    path('geoinfo/<int:pk>/', GeoNameRetrieveAPIView.as_view(), name='geo-info'),
]
from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from geoinfo_apiapp.models import GeoName
from geoinfo_apiapp.serializers import GeoNameSerializer
from geoinfo_apiapp.utils import get_difference_tzs


class GeoNameRetrieveAPIView(RetrieveAPIView):
    """
    API View for getting information about an object by id.
    """

    queryset = GeoName.objects.all()
    serializer_class = GeoNameSerializer

    @extend_schema(
        responses={
            200: GeoNameSerializer,
            404: OpenApiResponse(description='Empty response, object by id not found.')
        })
    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Get method returns object by id.
        """

        return super().get(request, *args, **kwargs)


class GeoNameListAPIView(ListAPIView):
    """
    API View for getting list of objects.
    Filter and search by objects implemented.
    """

    queryset = GeoName.objects.order_by('pk').all()
    serializer_class = GeoNameSerializer

    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        'name',
        'alternatenames',
    ]

    ordering_fields = [
        'geonameid',
    ]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='g1',
                description='A geographical object №1 for comparison.'
            ),
            OpenApiParameter(
                name='g2',
                description='A geographical object №2 for comparison.'
            ),
        ],
        responses={
            200: GeoNameSerializer,
            404: OpenApiResponse(description='Empty response, objects not found.'),
        })
    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Overriding the get method
        if the query string asks for `search` or compare `g1` and `g2`
        Returns a list of objects with all information,
        with comparison information, or a list of matches.
        """

        params = self.request.query_params

        if params.get('search'):
            response = self.list(request, *args, **kwargs)
            response.data['results'] = [i_obj['name'] for i_obj in response.data['results']]
            return response

        elif params.get('g1') and params.get('g2'):
            name_g1 = params.get('g1').capitalize()
            name_g2 = params.get('g2').capitalize()

            geo_object_1 = GeoName.objects.filter(
                Q(alternatenames__icontains=name_g1) | Q(name__icontains=name_g1)
            ).order_by('-population').first()
            geo_object_2 = GeoName.objects.filter(
                Q(alternatenames__icontains=name_g2) | Q(name__icontains=name_g2)
            ).order_by('-population').first()

            if geo_object_1 and geo_object_2:

                if geo_object_1.latitude > geo_object_2.latitude:
                    northern_object = geo_object_1.name
                else:
                    northern_object = geo_object_2.name

                if geo_object_1.timezone == geo_object_2.timezone:
                    timezone_same = True
                else:
                    timezone_same = False

                self.queryset = [geo_object_1, geo_object_2]
                response = self.list(request, *args, **kwargs)

                difference_tzs = get_difference_tzs(
                    geo_object_1.timezone,
                    geo_object_2.timezone,
                )
                comparison = {
                    'geographical_object_1': {
                        'name': geo_object_1.name,
                        'population': geo_object_1.population,
                        'latitude': geo_object_1.latitude,
                        'timezone': geo_object_1.timezone,
                    },
                    'geographical_object_2': {
                        'name': geo_object_2.name,
                        'population': geo_object_2.population,
                        'latitude': geo_object_2.latitude,
                        'timezone': geo_object_2.timezone,
                    },
                    'The object is located north': northern_object,
                    'Time zones the same': timezone_same,
                    'Time zone difference': difference_tzs,
                }
                response.data['comparison'] = comparison

                return response

            if not geo_object_1 and not geo_object_2:
                not_found_object = 's g1 and g2'
            elif geo_object_1 is None:
                not_found_object = ' g1'
            else:
                not_found_object = ' g2'

            return Response({f'Not found object{not_found_object} to comparison.'})
        return self.list(request, *args, **kwargs)

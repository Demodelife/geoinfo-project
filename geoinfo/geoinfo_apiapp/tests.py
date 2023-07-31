from django.db.models import Q
from django.test import TestCase
from django.urls import reverse
from geoinfo_apiapp.models import GeoName


class GeoNameRetrieveAPIViewTestCase(TestCase):
    """
    Test case for get object by id.
    """

    @classmethod
    def setUpClass(cls):
        """
        Creating a new object at the class level.
        """

        cls.object = GeoName.objects.create(
            geonameid=123456789,
            latitude=45.12345,
            longitude=45.12345,
            modification_date='2020-12-31'
        )

    @classmethod
    def tearDownClass(cls):
        """
        Deleting created object after tests.
        """

        cls.object.delete()

    def test_get_geo_object_by_id(self):
        """
        Method test.
        Tests getting objects by id.
        """

        response = self.client.get(
            reverse('geoinfo_apiapp:geo-info', kwargs={'pk': self.object.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.object.modification_date)


class GeoNameListAPIViewTestCase(TestCase):
    """
    Test case for getting list of objects.
    Implemented test filter and test search by objects.
    """

    fixtures = [
        'geo_objects_fixture.json',
    ]

    def test_get_list(self):
        """
        Method test.
        Tests getting a list of objects.
        """

        response = self.client.get(reverse('geoinfo_apiapp:geo-list'), {
            'page': 1,
            'count': 100,
        })

        self.assertQuerySetEqual(
            qs=GeoName.objects.order_by('pk')[:100],
            values=map(lambda g: g['geonameid'], response.data['results']),
            transform=lambda g: g.pk,
        )

    def test_search(self):
        """
        Method test.
        Tests getting a list of objects with query parameter `search`.
        """

        response = self.client.get(reverse('geoinfo_apiapp:geo-list'), {
            'search': 'Zh'
        })

        self.assertQuerySetEqual(
            qs=GeoName.objects.filter(name__contains='Zh').order_by('pk')[:100],
            values=response.data['results'],
            transform=lambda g: g.name,
        )

    def test_comparison(self):
        """
        Method test.
        Tests getting comparison with query parameters `g1` and `g2`.
        """

        response = self.client.get(reverse('geoinfo_apiapp:geo-list'), {
            'g1': 'Timonino',
            'g2': 'Strenevo',
        })

        self.assertQuerySetEqual(
            qs=GeoName.objects.filter(
                Q(name__icontains='Timonino') |
                Q(name__icontains='Strenevo')
            ).order_by('pk')[:100],
            values=map(lambda g: g['geonameid'], response.data['results']),
            transform=lambda g: g.pk,
        )

from django.core import serializers
from django.core.management import BaseCommand
from geoinfo_apiapp.models import GeoName
from os import path
from json import dump, loads


class Command(BaseCommand):
    """
    Command class to dump fixtures.
    """

    def handle(self, *args, **options):
        """
        Method handler for `dump_fixtures` command.
        """

        path_fixture = path.abspath(path.join('geoinfo_apiapp', 'fixtures', 'geo_objects_fixture.json'))

        def dump_fixtures():
            """
            Function to dump fixtures.
            """

            instances = GeoName.objects.order_by('pk')[:100]

            serialized_data = serializers.serialize('json', instances)
            data = loads(serialized_data)

            with open(path_fixture, 'w', encoding='utf-8') as file:
                dump(data, file)

        if path.exists(path_fixture):
            self.stdout.write('Fixtures already exists.')
        else:
            dump_fixtures()
            self.stdout.write(self.style.SUCCESS('Successfully dumped!'))

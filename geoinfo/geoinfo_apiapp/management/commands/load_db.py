from django.core.management import BaseCommand
from geoinfo_apiapp.models import GeoName
from os import path
from _decimal import Decimal


class Command(BaseCommand):
    """
    Command class to create instances.
    """

    def handle(self, *args, **options) -> None:
        """
        Method handler for `load_db` command.
        """

        path_dump = path.abspath(path.join('dump_data', 'RU.txt'))

        def load_instances() -> None:
            """
            Function to create instances.
            """

            with open(path_dump, 'r', encoding='utf-8') as file_load:
                load_data = file_load.readlines()

            instances = []

            for i_data in load_data:
                data = i_data.replace('\n', '').split('\t')

                instances.append(
                    GeoName(
                        geonameid=int(data[0]),
                        name=data[1],
                        asciiname=data[2],
                        alternatenames=data[3],
                        latitude=Decimal(data[4]),
                        longitude=Decimal(data[5]),
                        feature_class=data[6],
                        feature_code=data[7],
                        country_code=data[8],
                        cc2=data[9],
                        admin1_code=data[10],
                        admin2_code=data[11],
                        admin3_code=data[12],
                        admin4_code=data[13],
                        population=int(data[14]),
                        elevation=int(data[15] or 0),
                        dem=int(data[16]),
                        timezone=data[17],
                        modification_date=data[18]
                    )
                )

            GeoName.objects.bulk_create(instances)

        if GeoName.objects.all()[:10]:
            self.stdout.write('Instances already exists.')
        else:
            self.stdout.write('Creation instances...')
            load_instances()
            self.stdout.write(self.style.SUCCESS('Successfully created!'))

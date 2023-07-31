# Generated by Django 4.2.3 on 2023-07-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoName',
            fields=[
                ('geonameid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('asciiname', models.CharField(max_length=200)),
                ('alternatenames', models.CharField(blank=True, max_length=10000)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('feature_class', models.CharField(blank=True, max_length=1)),
                ('feature_code', models.CharField(blank=True, max_length=10)),
                ('country_code', models.CharField(blank=True, max_length=2)),
                ('cc2', models.CharField(blank=True, max_length=200)),
                ('admin1_code', models.CharField(blank=True, max_length=20)),
                ('admin2_code', models.CharField(blank=True, max_length=80)),
                ('admin3_code', models.CharField(blank=True, max_length=20)),
                ('admin4_code', models.CharField(blank=True, max_length=20)),
                ('population', models.BigIntegerField(blank=True, default=0)),
                ('elevation', models.IntegerField(blank=True, default=0)),
                ('dem', models.IntegerField(blank=True, default=0)),
                ('timezone', models.CharField(blank=True, max_length=40)),
                ('modification_date', models.DateField(blank=True)),
            ],
        ),
    ]

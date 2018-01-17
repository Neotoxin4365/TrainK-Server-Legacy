# Generated by Django 2.0 on 2018-01-17 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departureIndex', models.IntegerField()),
                ('arrivalIndex', models.IntegerField()),
                ('seat', models.CharField(max_length=15, null=True)),
                ('boardingGate', models.CharField(max_length=30, null=True)),
                ('nextTrip', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previousTrip', to='trip.Trip')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='info.Record')),
                ('relatedTrips', models.ManyToManyField(related_name='_trip_relatedTrips_+', to='trip.Trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

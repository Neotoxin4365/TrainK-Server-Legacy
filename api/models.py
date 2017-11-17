from django.db import models
from django.contrib.postgres import fields
from django.core.serializers.json import DjangoJSONEncoder


class Station(models.Model):
	name = models.CharField(max_length=10)
	telecode = models.CharField(max_length=5, blank=True)


class Train(models.Model):
	names = fields.ArrayField(models.CharField(max_length=10))
	telecode = models.CharField(max_length=50, primary_key=True)
	stops = fields.JSONField(encoder=DjangoJSONEncoder)

	def __str__(self):
		return self.name

	@property
	def name(self):
		nameStr = ''
		for name in self.names:
			nameStr += name + '/'
		return nameStr[:-1]


class Record(models.Model):
	departureDate = models.DateField()
	train = models.ForeignKey(Train)
	stops = fields.JSONField(encoder=DjangoJSONEncoder)


class Stop(models.Model):
	train = models.ForeignKey(Train)
	record = models.ForeignKey(Record)
	station = models.ForeignKey(Station)
	index = models.IntegerField()
	departureTime = models.DateTimeField()
	departureTimeAnticipated = models.BooleanField()
	arrivalTime = models.DateTimeField()
	arrivalTimeAnticipated = models.BooleanField()

	class Meta:
		managed = False

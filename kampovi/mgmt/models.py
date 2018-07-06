from django.db import models
from django.contrib.auth import get_user_model


class Radionica(models.Model):
	name = models.CharField(
		max_length=200
	)

	leader_name = models.CharField(
		max_length=200
	)

	description = models.CharField(
		max_length=200,
		null=True
	)

	kamp = models.ForeignKey(
		'Kamp',
		on_delete = models.CASCADE
	)
	
	start_time = models.TimeField(
		'Pocetak radonice',
		null=True
	)
	
	end_time = models.TimeField(
		'Kraj radonice',
		null=True
	)

	difficulties = (
		('b', 'Pocetna'),
		('e', 'Lagana'),
		('i', 'Srednja'),
		('a', 'Napredna'),
		('x', 'Experti'),
		('o', 'Olimpijci'),
	)

	difficulty = models.CharField(
		max_length=1,
		choices=difficulties,
		null=True
	)

	class Meta:
		verbose_name_plural = 'Radionice'

	def __str__(self):
		return self.name


class Kamp(models.Model):
	name = models.CharField(
		max_length=150
	)

	def __str__(self):
		return self.name

	start_date = models.DateField(
		'Pocetak kampa',
	)
	end_date = models.DateField(
		'Kraj kampa',
	)

	location = models.CharField(
		max_length = 200,
		default = 'Krk'
	)

	class Meta:
		verbose_name_plural = 'Kampovi'

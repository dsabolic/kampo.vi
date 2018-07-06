from django.db import models


class Radionica(models.Model):
	name = models.CharField(
		max_length = 200
	)

	leader_name = models.CharField(
		max_length = 200
	)

	description = models.CharField(
		max_length = 200,
		null=True
	)

	kamp = models.ForeignKey(
		'Kamp',
		on_delete = models.CASCADE
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

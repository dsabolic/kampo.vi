from django.db import models

class Kamp(models.Model):
	name = models.CharField(
		max_length=150
	)

	def __str__(self):
		return self.name

	start_date = models.DateTimeField(
		'Pocetak kampa'
	)
	end_date = models.DateTimeField(
		'Kraj kampa'
	)
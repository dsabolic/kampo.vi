from django.db import models

<<<<<<< HEAD
# Create your models here.
class Radionica(models.Model):
	name = models.CharField(
		max_length = 200
	)

	leader_name = models.CharField(
		max_length = 200
	)

	description = models.CharField(
		max_length = 200
	)

	def __str__(self):
		return self.name
=======
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
>>>>>>> 83897eecfd4b1c4ad9729d2d33c18167889543b0

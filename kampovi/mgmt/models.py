from django.db import models

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
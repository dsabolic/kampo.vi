from django.contrib import admin
from .models import Kamp, Radionica

class RadionicaAdmin(admin.ModelAdmin):
	fields = [
		'name',
		'leader_name',
		'description',
		'start_time',
		'end_time',
		'difficulty'
	]

class RadionicaInline(admin.StackedInline):
	model = Radionica
	extra = 1
 
class KampAdmin(admin.ModelAdmin):
	fields = [
		'name', 'location',
		('start_date', 'end_date')
	]

	inlines = [RadionicaInline]
	list_display = ('name', 'location', 'start_date', 'end_date')

admin.site.register(Kamp, KampAdmin)
admin.site.register(Radionica, RadionicaAdmin)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Kamp, Radionica

# Create your views here.
def index(request):
	kampovi_list = Kamp.objects.order_by('start_date')
	context = {
		'kampovi_list': kampovi_list
	}

	return render(request, 'mgmt/index.html', context)

def detail(request, kamp_id):
	kamp = get_object_or_404(Kamp, pk=kamp_id)
	radionice_list = kamp.radionica_set.all()
	return render(request, 'mgmt/detail.html', {'kamp': kamp, 'radionice_list': radionice_list})

def register(request, kamp_id):
	kamp = get_object_or_404(Kamp, pk=kamp_id)
	return render(request, 'mgmt/register.html', {'kamp': kamp})

def success(request, kamp_id):
	kamp = get_object_or_404(Kamp, pk=kamp_id)

	first_name = request.POST['first_name']
	last_name = request.POST['last_name']

	if len(first_name) == 0 or len(last_name) == 0:
		return render(
			request,
			'mgmt/register.html',
			{
				'kamp': kamp,
				'error_message': 'Morate unijeti ime i prezime!'
			}
		)

	return render(request, 'mgmt/success.html', {'kamp': kamp})
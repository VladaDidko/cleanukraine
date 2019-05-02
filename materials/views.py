from django.shortcuts import render
from .models import Type, Code, Waste, Station
from django.db.models import Q
from .filters import StationFilter

def codes(request):
	codes = Code.objects.all()
	types = Type.objects.all()

	query = request.GET.get("q")
	if query:
		codes = codes.filter(
			Q(abbreviation__icontains = query) |
			Q(description__icontains = query)
			).distinct()

	context = {
	'types': types,
	'codes': codes,
	}

	return render(request,"materials/codes.html",context)

def wastes(request):
	wastes = Waste.objects.all()
	query = request.GET.get("q")
	if query:
		wastes = wastes.filter(
			Q(title__icontains = query) |
			Q(description__icontains = query) |
			Q(utilization__icontains = query)
			).distinct()
		
	context = {
	'wastes': wastes
	}

	return render(request,"materials/wastes.html",context)

def map(request):
	stations = Station.objects.all()
	query = request.GET.get("q")
	if query:
		stations = stations.filter(
			Q(title__icontains = query) |
			Q(description__icontains = query) |
			Q(address__icontains = query)
			).distinct()

	context = {
	'stations':stations
	}

	return render(request,"materials/map.html",context)

def search(request):
    stations = Station.objects.all()
    station_filter = StationFilter(request.GET, queryset=stations)
    return render(request, 'materials/map.html', {'filter': station_filter})
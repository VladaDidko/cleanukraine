from django.shortcuts import render
from .models import Type, Code, Waste

def codes(request):
	codes = Code.objects.all()
	types = Type.objects.all()
	context = {
	'types': types,
	'codes': codes,
	}

	return render(request,"materials/codes.html",context)

def wastes(request):
	wastes = Waste.objects.all()
	context = {
	'wastes': wastes
	}

	return render(request,"materials/wastes.html",context)
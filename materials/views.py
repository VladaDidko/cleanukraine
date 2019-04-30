from django.shortcuts import render
from .models import Type, Code

def home(request):
	codes = Code.objects.all()
	types = Type.objects.all()
	context = {
	'types': types,
	'codes': codes
	}

	return render(request,"materials/codes.html",context)
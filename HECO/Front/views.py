from django.shortcuts import render
from django.http import HttpResponse
from .models import Raw_Data
# Create your views here.
def Home(request):
    raw = Raw_Data.obje
    return render(request, 'Homepage.html')
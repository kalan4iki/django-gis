from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from bot.models import KNDhistor, DIPhistor
# Create your views here.


def index(request):
    knd = KNDhistor.objects.all()
    dip = DIPhistor.objects.all()
    return render(request, 'sites/index.html', {'knd': knd, 'dip': dip})

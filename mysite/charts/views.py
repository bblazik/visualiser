from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from . import sample


def index(request):
    sum = sample.sumTwo()
    context = {'sum': sum}
    return render(request, 'charts/index.html', context)
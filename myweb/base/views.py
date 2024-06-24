from django.shortcuts import render
from django.http import HttpResponse
from .models import Talents


# Create your views here.
def home(request):
    talents = Talents.objects.all()
    for talent in talents:
        print(talent)
    context = {"talents": talents}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


def test(request):
    return render(request, 'base/test.html')

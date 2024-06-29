from django.shortcuts import render
from django.http import HttpResponse
from .models import Talents, User


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


def profile(request, pk):
    user = User.objects.get(id=pk)
    talents = user.talents.all()
    context = {"talents": talents}
    return render(request, 'base/profile.html', context)

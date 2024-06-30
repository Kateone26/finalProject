from django.shortcuts import render
from django.http import HttpResponse
from .models import Talents, User, Category
from django.db.models import Q


# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    talents = Talents.objects.filter(Q(positions__name__icontains=q) | Q(bio__icontains=q) | Q(talentCode__icontains=q) | Q(skills__name__icontains=q) | Q(category__name__icontains=q)).distinct()
    # talents = list(set(talents))
    # talents = Talents.objects.all()
    categories = Category.objects.all()
    heading = "Freelance Talent Marketplace"
    context = {"talents": talents, "heading": heading, "categories": categories}
    # print(talents[1].users.all())
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


def test(request):
    return render(request, 'base/test.html')


def profile(request, pk):
    user = User.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    talents = user.talents.filter(Q(positions__name__icontains=q) | Q(bio__icontains=q) | Q(talentCode__icontains=q) | Q(skills__name__icontains=q) | Q(category__name__icontains=q)).distinct()
    # talents = user.talents.all()
    categories = Category.objects.all()
    heading = "My Favourite Freelancers"
    context = {"talents": talents, "heading": heading, "categories": categories}
    return render(request, 'base/profile.html', context)

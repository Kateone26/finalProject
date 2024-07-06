from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Talents, User, Category
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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


@login_required(login_url='login')
def about(request):
    return render(request, 'base/about.html')


def test(request):
    return render(request, 'base/test.html')


@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    talents = user.talents.filter(Q(positions__name__icontains=q) | Q(bio__icontains=q) | Q(talentCode__icontains=q) | Q(skills__name__icontains=q) | Q(category__name__icontains=q)).distinct()
    # talents = user.talents.all()
    categories = Category.objects.all()
    heading = "My Favourite Freelancers"
    context = {"talents": talents, "heading": heading, "categories": categories}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def adding(request, id):
    user = request.user
    talent = Talents.objects.get(id=id)
    user.talents.add(talent)
    return redirect('profile', request.user.id)


@login_required(login_url='login')
def delete(request, id):
    obj = Talents.objects.get(id=id)

    if request.method == "POST":
        request.user.talents.remove(obj)
        return redirect('profile', request.user.id)

    return render(request, 'base/delete.html', {'obj': obj})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile', request.user.id)

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            pass

    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')

def registration(request):
    return render(request, 'base/registration.html')



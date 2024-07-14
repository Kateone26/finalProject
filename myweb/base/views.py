from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Talents, User, Category, Position
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, TalentForm, UserForm
from .seeder import seeder_func
from django.contrib import messages



# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    seeder_func()
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
    # talents = list(dict.fromkeys(talents))
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
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'User or password is not correct!')

    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')

def registration(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile', user.id)
        else:
            messages.error(request, 'Follow instructions while creating password')

    context = {'form': form}
    return render(request, 'base/registration.html', context)


def add_cv(request):
    positions = Position.objects.all()
    categories = Category.objects.all()
    form = TalentForm()

    if request.method == 'POST':
        talent_position = request.POST.get('position')
        talent_category = request.POST.get('category')

        position, created = Position.objects.get_or_create(name=talent_position)
        category, created = Category.objects.get_or_create(name=talent_category)

        form = TalentForm(request.POST)

        new_talent = Talents(image=request.FILES['image'], bio=form.data['bio'], file=request.FILES['file'], creator=request.user)

        # this code will NOT let us upload pdf folders with same names:
        if not Talents.objects.filter(file=request.FILES['file']):
            new_talent.save()
            new_talent.positions.add(position)
            new_talent.category.add(category)
        else:
            messages.error(request, 'File with the same name already exists')

        # this code will let us upload pdf folders with same names:
        # new_talent.save()
        # new_talent.positions.add(position)
        # new_talent.category.add(category)
        return redirect('home')

    context = {'form': form, 'positions': positions, 'categorys': categories}
    return render(request, 'base/add_cv.html', context)


def reading(request, id):
    cv_file = Talents.objects.get(id=id)
    return render(request, 'base/reading.html', {'cv_file': cv_file})


def delete_cv(request, id):
    obj = Talents.objects.get(id=id)

    if request.method == "POST":
        obj.image.delete()
        obj.file.delete()
        obj.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': obj})


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)

    context = {'form': form}
    return render(request, 'base/update_user.html', context)



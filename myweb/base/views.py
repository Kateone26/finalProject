from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Talents, User, Category, Position
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, TalentForm


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
            pass

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

        new_talent = Talents(image=request.FILES['image'], bio=form.data['bio'], file=request.FILES['file'])

        new_talent.save()
        new_talent.positions.add(position)
        new_talent.category.add(category)
        return redirect('home')

    context = {'form': form, 'position': positions, 'category': categories}
    return render(request, 'base/add_cv.html', context)










# //////////////////////////////////////////////////////////////////////////////////
# ///////// doesnt submit but shows me the list of positions and categories

# def add_cv(request):
#     positions = Position.objects.all()
#     categories = Category.objects.all()
#     form = TalentForm()
#
#     if request.method == 'POST':
#         form = TalentForm(request.POST, request.FILES)
#         if form.is_valid():
#             talent_position = request.POST.get('position')
#             talent_category = request.POST.get('category')
#
#             position, created = Position.objects.get_or_create(name=talent_position)
#             category, created = Category.objects.get_or_create(name=talent_category)
#
#             new_talent = form.save(commit=False)
#             new_talent.save()
#             new_talent.positions.add(position)
#             new_talent.category.add(category)
#             return redirect('home')
#
#     context = {'form': form, 'positions': positions, 'categories': categories}
#     return render(request, 'base/add_cv.html', context)






# ///////////////////////////////////////////////////////////////////////
# ///////// doesnt submit but shows me the list of positions and categories

# def add_cv(request):
#     positions = Position.objects.all()
#     categories = Category.objects.all()
#     form = TalentForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             talent_position_name = form.cleaned_data['position']
#             talent_category_name = form.cleaned_data['category']
#
#             # Retrieve or create Position and Category objects
#             position, created = Position.objects.get_or_create(name=talent_position_name)
#             category, created = Category.objects.get_or_create(name=talent_category_name)
#
#             # Create a new Talents instance
#             new_talent = form.save(commit=False)
#             new_talent.positions.add(position)
#             new_talent.category.add(category)
#             new_talent.save()
#
#             return redirect('home')
#
#     context = {'form': form, 'positions': positions, 'categories': categories}
#     return render(request, 'base/add_cv.html', context)
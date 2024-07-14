from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Talents(models.Model):
    talentCode = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    # positionName = models.CharField(max_length=100)
    positions = models.ManyToManyField(Position, related_name='talents')
    bio = models.TextField(max_length=200)
    # skills = models.CharField(max_length=500)
    skills = models.ManyToManyField(Skill, related_name='talents')
    category = models.ManyToManyField(Category, related_name='talents')
    file = models.FileField(null=True)
    creator = models.ForeignKey('User', on_delete=models.SET("Unknown creator"), related_name='created_talents')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ["-bio"]
        ordering = ["created"]

    def __str__(self):
        return f"{self.talentCode} {self.positions}"


class User(AbstractUser):
    talents = models.ManyToManyField(Talents, related_name='users', blank=True)
    avatar = models.ImageField(null=True, default='reditprof.png')
    user_bio = models.TextField(null=True)


# name / level / flag / country / hourly rate / monthly rate / categories / language skills / industries / personal info / education / centificates and trainings / experience / projects /
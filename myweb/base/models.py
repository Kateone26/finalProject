from django.db import models

# Create your models here.


class Talents(models.Model):
    talentCode = models.CharField(max_length=20)
    image = models.CharField(max_length=300)
    positionName = models.CharField(max_length=100)
    bio = models.TextField(max_length=200)
    skills = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.talentCode} {self.positionName}"

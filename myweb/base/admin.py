from django.contrib import admin
from . models import Talents, Position, Skill, User
# Register your models here.

admin.site.register(Talents)
admin.site.register(Position)
admin.site.register(Skill)
admin.site.register(User)
from django.contrib import admin
from . models import Talents, Position, Skill, User, Category, Comment
# Register your models here.

admin.site.register(Talents)
admin.site.register(Position)
admin.site.register(Skill)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Comment)
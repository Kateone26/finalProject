from django.contrib.auth.forms import UserCreationForm
from .models import User, Talents
from django.forms import ModelForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # fields = '__all__'


class TalentForm(ModelForm):
    class Meta:
        model = Talents
        fields = '__all__'


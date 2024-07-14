from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('test', views.test, name='test'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('adding/<str:id>', views.adding, name='adding'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('registration', views.registration, name='registration'),path('add', views.add_cv, name='add'),
    path('reading/<str:id>', views.reading, name='reading'),
    path('delete_cv/<str:id>', views.delete_cv, name='delete_cv'),
]

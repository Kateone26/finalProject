from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_routes),
    path('talents/', views.get_talents),
    path('talents/<str:id>', views.get_talent)
]

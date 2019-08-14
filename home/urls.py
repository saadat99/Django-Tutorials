from django.conf.urls import url
from home.views import HomeView
from . import views

from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('connect/(<operation>.+)/(<pk>\d+)/', views.change_friends, name='change_friends')
]

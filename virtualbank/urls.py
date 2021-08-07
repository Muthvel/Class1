from django.urls import path
from . import views
urlpatterns = [
path('', views.welcome),
path('existing', views.greeting),
]

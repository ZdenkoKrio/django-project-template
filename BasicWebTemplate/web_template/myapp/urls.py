from django.urls import path
from .views import myapp

urlpatterns = [
    path("myapp/", myapp, name="myapp"),
]
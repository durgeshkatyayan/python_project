from django.urls import path

from . import views
from .views import sec

urlpatterns = [
    path("", views.index, name="index"),
    # path('name/',sec),
]
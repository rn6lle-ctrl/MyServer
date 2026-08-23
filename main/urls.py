from django.urls import path
from . import views

urlpatterns = [path("",views.home,name="home"),
               path("vremya/",views.время_сейчас,name="время сейчас"),
               path("obomne/",views.обомне, name="Обо мне"),
               path("info/", views.info, name="До нового года"),
               path("add/", views.add_task, name="add_task"),]

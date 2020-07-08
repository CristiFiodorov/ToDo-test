from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('todo/', views.index, name='index'),
    path("<int:id>", views.list_created, name="list_created"),
    path('create/', views.create, name='create'),
    path("view/", views.view, name="view"),
]

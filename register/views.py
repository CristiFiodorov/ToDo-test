from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.urls import reverse

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('todo_home'))
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})

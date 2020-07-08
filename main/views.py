from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import CreateNewList
from . models import ToDoList
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    return render(request, 'main/todo.html', {})


@login_required(login_url='/login/')
def list_created(request, id):
    ls = ToDoList.objects.get(id=id)

    if ls in request.user.todolist.all():

        if request.method == "POST":
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    p = request.POST

                    if "clicked" == p.get("c"+str(item.id)):
                        item.complete = True
                    else:
                        item.complete = False

                    if "text" + str(item.id) in p:
                        item.text = p.get("text" + str(item.id))

                    item.save()

            elif request.POST.get("add"):
                newItem = request.POST.get("new")
                if newItem != "":
                    ls.item_set.create(text=newItem, complete=False)
                else:
                    print("invalid")

        return render(request, "main/list_created.html", {"ls": ls})
    else:
        return render(request, "main/view.html", {})


@login_required(login_url='/login/')
def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)

            return HttpResponseRedirect(reverse('main:list_created', args=(t.id,)))

    else:
        form = CreateNewList()
    return render(request, 'main/create.html', {'form': form})


@login_required(login_url='/login/')
def view(request):
    l = ToDoList.objects.all()
    return render(request, "main/view.html", {})

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def home(request):
    return render(request, "landing_page.html")

def todos(request):
    items = Item.objects.all()
    return render(request, "todos.html", {"todos": items})

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "list.html", {"ls":ls})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "create.html", {"form":form})
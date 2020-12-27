from django.shortcuts import render

from .forms import TodoAddForm
from .models import Todo


def home(request):
    return render(request, "todo/home.html")


def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, "todo/todo_list.html", context)


def todo_create(request):
    form = TodoAddForm()
    context = {
        'form': form
    }
    return render(request, "todo/todo_create.html", context)

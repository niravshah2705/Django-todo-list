from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    login_user = request.user
    return render(request, 'todos/index.html', {'todo_list': Todo.objects.filter(user=login_user).order_by('-created_at'), 'user': login_user})


def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title, user=request.user)

    return redirect('todos:index')


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True

    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')

import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def todaytodos(request):
    if request.method == 'POST':
        if request.POST['description']:
            print(request.POST['description'])
            todo = Todo()
            todo.description = request.POST['description']
            todo.save()
        return redirect('today')
    else:
        todos = Todo.objects.all().filter(date__gte=datetime.date.today())
        return render(request, 'todo/todos.html', {'todos': todos})

def remove(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('today')

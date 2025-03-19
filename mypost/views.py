from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Read - List All Tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'mypost/task_list.html', {'tasks': tasks})

# Create - Add a Task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'mypost/task_form.html', {'form': form})

# Update - Edit a Task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'mypost/task_form.html', {'form': form})

# Delete - Remove a Task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'mypost/task_confirm_delete.html', {'task': task})

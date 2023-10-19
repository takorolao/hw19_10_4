from django.shortcuts import render
from .forms import IceCreamForm


def create_ice_cream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            # редирект на страницу с инфой о мороженом 
    else:
        form = IceCreamForm()
    return render(request, 'tasks/ice_cream_form.html', {'form': form})

def task_list(request):
    tasks = ['Task 1', 'Task 2', 'Task 3']  # список задач
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = f'Task {task_id}'  # получение задачи из бд
    return render(request, 'tasks/task_detail.html', {'task': task})

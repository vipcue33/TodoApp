from django.shortcuts import render
from django.http import JsonResponse
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        
        # Create a new task object and save it to the database
        task = Todo.objects.create(
            title=title,
            description=description,
            due_date=due_date
        )
        task.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
@csrf_exempt
def get_tasks(request):
    if request.method == 'GET':
        tasks = Todo.objects.all().values()
        tasks_list = list(tasks)
        return JsonResponse(tasks_list, safe=False)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
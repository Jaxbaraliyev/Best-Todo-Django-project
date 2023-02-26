from django.shortcuts import render, redirect
from django.views import View
from .models import *

class TodoView(View):
    def get(self, request):
        todos = Todo.objects.all()
        active_count=todos.filter(is_active=True).count()
        data = {"todos":todos.order_by('-is_important'),'all_count':todos.count(),'active_count':active_count,'deactive_count':todos.count()-active_count}
        return render(request, 'todos.html', data)

    def post(self, request):
        if request.method == 'POST':
            title=request.POST.get('t',False)
            is_important=request.POST.get('is_important',False)
            if title:
                todo=Todo(title=title)
                if is_important:
                    todo.is_important=True
                todo.save() 
            else:
                pass 
        return redirect('home')

def todo_delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect('home')
        

def todo_important(request, pk):
    todo = Todo.objects.get(id=pk)
    is_active = int(request.GET.get('is_active'))
    if is_active == 0:
        todo.is_important = True
    else:
        todo.is_important=False    
    # todo.is_important = not(is_active)
    todo.save()
    return redirect('home')

def todo_active(request, pk):
    todo = Todo.objects.get(id=pk)
    is_search = int(request.GET.get('is_search'))
    if is_search == 0:  
        todo.is_active = True
    else:
        todo.is_active = False
    todo.save()
    return redirect('home')


def todo_all_delete(request):
    Todo.objects.filter(is_active=False).delete()
    return redirect('home')



        



from django.shortcuts import render
from .models import Todo
from .form import Tform
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    if request.method == "POST":
        form = Tform(request.POST or None)

        if form.is_valid():
            form.save()
            todo_list = Todo.objects.all()
            messages.success(request,("Task has been added"))
            return render(request,'todo/index.html',{'todo_here':todo_list})
    else:
        todo_list = Todo.objects.all()
        return render(request,'todo/index.html',{'todo_here':todo_list})
   
def deletes(request,id):
    t = Todo.objects.get(id=id)
    t.delete()

    messages.success(request,("Task has been Deleted!!!"))
    return redirect("home")



def m_com(request,id):
    t = Todo.objects.get(id=id)
    t.completed = True 
    t.save()
    return redirect('home')

def m_incom(request,id):
    t = Todo.objects.get(id=id)
    t.completed = False
    t.save()
    return redirect('home')

def edit(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        form = Tform(request.POST or None, instance=todo)
 
        if form.is_valid():
            form.save()
            messages.success(request, ('Task has been edited!'))
            return redirect('home')
    else:
        todo = Todo.objects.get(id=id)
        return render(request, 'todo/edit.html', {'todo': todo})
    
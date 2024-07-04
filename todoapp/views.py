from django.shortcuts import render,redirect

from django.http import HttpResponse

from todoapp.models import Todo,TodoForm
# Create your views here.


def home(request):
    todo=Todo.objects.all().order_by("-id")
    context={
        'todo':todo,
        'form':TodoForm
    }
    if request.method=="POST":
        data=request.POST
        todo=TodoForm(data)
        if todo.is_valid():
            todo.save()
            
    return render(request,'todoapp/home.html',{'data':context})

def update(request,id):
    targettodo=Todo.objects.get(id=id)
    context={
        "todo":targettodo
    }
    if request.method=="POST":
        todo=request.POST
        text=todo['todotext']
        todoid=todo['todoid']
        print(text)
        print(todoid)
        obj=Todo.objects.get(id=todoid)
        obj.text=text
        obj.save()
        return redirect("/")
    return render(request,"todoapp/update.html",context)

def delete(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")
    
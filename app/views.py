from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse

from app.models import ToDoList, ToDo

def index(request):
    to_do_list = ToDoList.objects.all()
    context = {
        'to_do_list': to_do_list,
    }
    return render(request, 'app/index.html', context)

class ToDoListCreateView(generic.CreateView):
    model = ToDoList
    fields = ('title',)


class ToDoListDetailView(generic.DetailView):
    model = ToDoList


class ToDoCreateView(generic.CreateView):
    model = ToDo
    fields = ('title', 'description')

    def form_valid(self, form):
        form.instance.to_do_list_id = self.kwargs.get('pk')
        return super(ToDoCreateView, self).form_valid(form)


class ToDoDetailView(generic.DetailView):
    model = ToDo


class ToDoUpdateView(generic.UpdateView):
    model = ToDo
    fields = ('title', 'description')


class ToDoListUpdateView(generic.UpdateView):
    model = ToDoList
    fields = ('title',)

def DeleteTask(request, pk):
    """ Elimino una tarea """
    todo = ToDo.objects.get(pk=pk)
    todo.delete()
    return redirect(todo)

def TaskDone(request, pk):
    """ Acutalizo el estado de la tarea """
    todo = ToDo.objects.get(pk=pk)
    todo.done = not todo.done
    todo.save()
    return redirect(todo)

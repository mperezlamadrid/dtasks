from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.utils import timezone
import datetime
import json

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

    def get_context_data(self, **kwargs):
        this_month = datetime.datetime.now().month
        context = super(ToDoListDetailView, self).get_context_data(**kwargs)
        report = self.request.GET.get('report')
        to_do_list = ToDoList.objects.get(pk=self.kwargs.get('pk'))
        if report == "all-completed-tasks":
            context["tasks"] = to_do_list.todo_set.filter(done=True)
        elif report == "completed-tasks":
            context["tasks"] = to_do_list.todo_set.filter(done=True, created_at__month=this_month)
        elif report == "all-pending-tasks":
            context["tasks"] = to_do_list.todo_set.filter(done=False)
        elif report == "pending-tasks":
            context["tasks"] = to_do_list.todo_set.filter(done=False, created_at__month=this_month)
        else:
            context["tasks"] = to_do_list.todo_set.all()
        return context

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
    if request.is_ajax():
        """ Elimino una tarea """
        todo = ToDo.objects.get(pk=pk)
        todo.delete()
        data = {'deleted': True, 'todo_id': pk}
        return JsonResponse(data)
    else:
        return redirect(todo)

def TaskDone(request, pk):
    """ Acutalizo el estado de la tarea """
    if request.is_ajax():        
        now = timezone.now()
        todo = ToDo.objects.get(pk=pk)
        diff = now - todo.created_at
        if diff.days <= 30 or diff.days > 30 and not todo.done:
            todo.done = not todo.done
            todo.save()
            data = {'updated':todo.done, 'todo_id': todo.id}
            return JsonResponse(data)
        else:
            response = JsonResponse({'error': 'You can not mark this task as not finished'}, status=405)
            return response
    else:
        return redirect(todo)

def DeleteList(request, pk):
    if request.is_ajax():
        """ Elimino una Lista """
        todolist = ToDoList.objects.get(pk=pk)
        todolist.delete()
        data = {'deleted': True, 'todolist_id': pk}
        return JsonResponse(data)
    else:
        return redirect(todolist)

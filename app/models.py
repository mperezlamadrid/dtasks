from django.db import models
from django.utils import timezone
from django.urls import reverse

class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def to_do_count(self):
        return self.todo_set.all().count()

    def get_absolute_url(self):
        return reverse('app:list_detail', args=(self.pk,))


class ToDo(models.Model):
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:list_detail', args=(self.to_do_list_id,))

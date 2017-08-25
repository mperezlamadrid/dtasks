from django.contrib import admin
from .models import ToDoList, ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'done', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['done']


class ToDoInline(admin.TabularInline):
    fields = ('title', 'description', 'done')
    # readonly_fields = ('votes',)
    model = ToDo
    extra = 1


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    inlines = [ToDoInline]


admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(ToDo, ToDoAdmin)

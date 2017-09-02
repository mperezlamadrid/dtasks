from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "app"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # URLs for Task List
    url(r'^list/create$', views.ToDoListCreateView.as_view(), name='create_list'),
    url(r'^list/(?P<pk>[0-9]+)/$', views.ToDoListDetailView.as_view(), name='list_detail'),
    url(r'^list/(?P<pk>[0-9]+)/edit$', views.ToDoListUpdateView.as_view(), name='update_list'),
    url(r'^delete_list/(?P<pk>[0-9]+)/$', views.DeleteList, name='delete_list'),
    # URLs for Task
    url(r'^list/(?P<pk>[0-9]+)/create_task$', views.ToDoCreateView.as_view(), name='create_task'),
    url(r'^task/(?P<pk>[0-9]+)/edit$', views.ToDoUpdateView.as_view(), name='update_task'),
    url(r'^delete_task/(?P<pk>[0-9]+)/$', views.DeleteTask, name='delete_task'),
    url(r'^task_done/(?P<pk>[0-9]+)/$', views.TaskDone, name='task_done'),
    # URLs for reports
    # url(r'^reports/(?P<pk>[0-9]+)/$', views.ToDoListReportsView, name='list_reports'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

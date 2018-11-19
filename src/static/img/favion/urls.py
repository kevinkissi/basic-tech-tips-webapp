from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^tasks/update/(?P<pk>\d+)/$', views.TaskUpdateView.as_view(), name='task-update'),
    url(r'^tasks/ajax/(?P<pk>\d+)/$', views.TaskAJAXView.as_view(), name='task-ajax-detail')
]
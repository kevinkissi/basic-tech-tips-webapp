import json

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from braces.views import JSONResponseMixin  # http://django-braces.readthedocs.org/

from .models import Task
from .forms import TaskForm


class AjaxableResponseMixin(object):
    """ Ajax form based on the django docs example.
    
    https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/#ajax-example
    https://docs.djangoproject.com/en/dev/topics/class-based-views/mixins/#more-than-just-html
    """

    def render_to_json_response(self, context, **response_kwargs):
        """Render a json response of the context."""

        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)
    
    def form_invalid(self, form):
        response = super(AjaxableRetosponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)

        return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            # Request is ajax, send a json response
            data = {
                'pk': self.object.pk,
            }
            return self.render_to_json_response(data)

        return response  # Request isn't ajax, send normal response


class TaskAJAXView(JSONResponseMixin, generic.DetailView):
    """Model view  for displaying tasks in JSON."""
  
    model = Task
    content_type = 'application/javascript'
    json_dumps_kwargs = {'indent': 2}

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context_dict = {
          'title': self.object.title,
          'description': self.object.description,
        }

    return self.render_json_response(context_dict)


class TaskUpdateView(AjaxableResponseMixin, generic.UpdateView):
    """Update view that handles both html and ajax updates."""

    model = Task
    form_class = TaskForm
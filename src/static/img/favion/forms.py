from django.db import forms


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

from django import forms
from webapp.models import Task, Type, Status


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.SelectMultiple)
        status = forms.ModelMultipleChoiceField(queryset=Status.objects.all(), widget=forms.RadioSelect)
        fields = {'description', 'detailed_description', 'status', 'type'}
        labels = {
            'description': 'Описание',
            'detailed_description': 'Подробно',
            'status': 'Статус',
            'type': 'Тип',
        }
        widgets = {
            'status': forms.RadioSelect,
            'type': forms.SelectMultiple
        }


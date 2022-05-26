from django.forms import ModelForm
from .models import Todo


class IsCompletedForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["completed"]

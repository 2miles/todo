
from django.views.generic import ListView
from .models import Todo
# Create your views here.

class TodoListView(ListView): 
    template_name = 'todo_list.html'
    def get_queryset(self):
      return Todo.objects.order_by('id')
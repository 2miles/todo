
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo
# Create your views here.

class TodoListView(ListView): 
    model = Todo
    template_name = 'todo_list.html'

    def get_queryset(self):
      """Returns Todos that belong to the current user, oldest first"""
      return Todo.objects.filter(user=self.request.user).order_by('start_date')


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoUpdateView(UpdateView):
    model = Todo
    fields = (
        "title",
        "description", 
        "completed"
    )
    template_name = 'todo_edit.html'
    success_url = reverse_lazy("todo_list")
  

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy("todo_list")

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Todo

# Create your views here.


class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"

    def get_queryset(self):
        """Returns un-completed Todos that belong to the current user, oldest first"""
        return (
            Todo.objects.filter(user=self.request.user)
            .exclude(completed=True)
            .order_by("start_date")
        )


class TodoCompletedView(ListView):
    model = Todo
    template_name = "todo_list.html"

    def get_queryset(self):
        """Returns completed Todos that belong to the current user, newest first"""
        return (
            Todo.objects.filter(user=self.request.user)
            .exclude(completed=False)
            .order_by("-start_date")
        )


class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo_detail.html"

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ("title", "description", "completed")
    template_name = "todo_edit.html"
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo_delete.html"
    success_url = reverse_lazy("todo_list")


class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo_new.html"
    fields = (
        "title",
        "description",
    )
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)

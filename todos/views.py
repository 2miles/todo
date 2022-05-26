from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.dates import (
    ArchiveIndexView,
    YearArchiveView,
    MonthArchiveView,
)
from django.urls import reverse_lazy

from .forms import IsCompletedForm
from .models import Todo

# Create your views here.


class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"

    def get_context_data(self, **kwargs):
        form = IsCompletedForm()
        # Call the base implementation first to get the context
        context = super(TodoListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        item_count = Todo.objects.filter(
            user=self.request.user, completed=False
        ).count()
        context["item_count"] = item_count
        context["form"] = form
        return context

    def get_queryset(self):
        """Returns un-completed Todos that belong to the current user, newest first"""
        return (
            Todo.objects.filter(user=self.request.user)
            .exclude(completed=True)
            .order_by("-start_date")
        )


def completed_view(request, pk):
    object = Todo.objects.get(id=pk)
    if object.user == request.user:
        object.completed = True
        object.finish_date = datetime.now()
        object.save()
    return HttpResponseRedirect("/todos/")


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


class TodoMonthArchiveView(MonthArchiveView):
    model = Todo
    template_name = "todo_archive_month.html"
    date_field = "finish_date"
    queryset = Todo.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by("finish_date")


class TodoYearArchiveView(YearArchiveView):
    model = Todo
    template_name = "todo_archive_year.html"
    date_field = "finish_date"
    queryset = Todo.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TodoArchiveIndexView(ArchiveIndexView):
    model = Todo
    template_name = "todo_archive.html"
    date_field = "finish_date"
    queryset = Todo.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ("title", "description", "completed")
    template_name = "todo_edit.html"
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form) -> HttpResponse:
        todo = self.object
        if form.instance.completed and todo.finish_date is None or False:
            todo.finish_date = datetime.now()
        if not form.instance.completed:
            todo.finish_date = None
        return super().form_valid(form)


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

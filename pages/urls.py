# pages/urls.py
from django.urls import path

from todos.views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
]

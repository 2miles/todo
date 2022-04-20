# pages/urls.py
from django.urls import path, include

from todos.views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
]

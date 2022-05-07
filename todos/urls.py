from django.urls import path

from .views import (
    TodoListView,
    TodoCompletedView,
    TodoDetailView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCreateView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("completed/", TodoCompletedView.as_view(), name="todo_complete"),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    path("<int:pk>/edit/", TodoUpdateView.as_view(), name="todo_edit"),
    path("<int:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
    path("new/", TodoCreateView.as_view(), name="todo_new"),
]

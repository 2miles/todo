from django.urls import path

from .views import (
    TodoListView,
    TodoCompletedView,
    TodoArchiveIndexView,
    TodoYearArchiveView,
    TodoMonthArchiveView,
    TodoDetailView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCreateView,
)
from .views import completed_view

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("completed/", TodoCompletedView.as_view(), name="todo_complete"),
    path("archive/", TodoArchiveIndexView.as_view(), name="todo_archive"),
    path(
        "archive/<int:year>/<str:month>/",
        TodoMonthArchiveView.as_view(month_format="%b"),
        name="todo_archive_month",
    ),
    path(
        "archive/<int:year>/", TodoYearArchiveView.as_view(), name="todo_archive_year"
    ),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    path("<int:pk>/edit/", TodoUpdateView.as_view(), name="todo_edit"),
    path("<int:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
    path("<int:pk>/complete/", completed_view, name="todo_completed"),
    path("new/", TodoCreateView.as_view(), name="todo_new"),
]

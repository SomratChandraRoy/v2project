from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<str:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("update/<str:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<str:pk>/", TaskDeleteView.as_view(), name="task_delete"),
]

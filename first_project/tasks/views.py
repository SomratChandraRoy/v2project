from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class TaskListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    model = Task

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    login_url = reverse_lazy("login")
    model = Task

    def test_func(self):
        return self.request.user == self.get_object().author


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    model = Task
    fields = ("task", "is_complete")
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = Task
    fields = ("task", "is_complete")
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("task_list")

    def test_func(self):
        return self.request.user == self.get_object().author


class TaskDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    model = Task
    success_url = reverse_lazy("task_list")

    def test_func(self):
        return self.request.user == self.get_object().author

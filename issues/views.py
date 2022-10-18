from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Issue, Status

class IssueListView(ListView):
    template_name = "posts/list.html"
    model = Issue
    status = "to do"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name=self.status)
        context['post_list'] = Issue.objects.filter(
                                        status=pending_status).order_by(
                                            'created_on').reverse()
        return context



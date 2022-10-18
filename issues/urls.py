from django.urls import path
from .views import IssueListView


urlpatterns = [
    path('issues/', IssueListView.as_view(), name='list'),
]
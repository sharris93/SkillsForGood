# This file will act as a router ONLY for the charities data entity
from django.urls import path
from .views import CharityListView, CharityDetailView

urlpatterns = [
    path('', CharityListView.as_view()), # index, create - /api/charities
    path('<int:pk>/', CharityDetailView.as_view())
]
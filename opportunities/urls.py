from django.urls import path
from .views import OpportunityListView, OpportunityDetailView

urlpatterns = [
    path('', OpportunityListView.as_view()), # /api/opportunities - List Route
    path('<int:pk>/', OpportunityDetailView.as_view()) # /api/opportunities/:pk - Detail route
]
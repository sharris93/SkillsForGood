from django.urls import path
from .views import OpportunityListView, OpportunityDetailView, OpportunityMatchedView

urlpatterns = [
    path('', OpportunityListView.as_view()), # /api/opportunities/ - List Route
    path('matched/', OpportunityMatchedView.as_view()), # /api/opportunities/matched/
    path('<int:pk>/', OpportunityDetailView.as_view()), # /api/opportunities/:pk/ - Detail route
]
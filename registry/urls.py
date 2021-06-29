from django.urls import path
from .views import PatientsView,VisitsView

urlpatterns = [
    path('patients', PatientsView.as_view()),
    path('visits',VisitsView.as_view())
]
from django.urls import path
from .views import PatientsView, VisitsView, SymptomsView, PrescriptionsView

urlpatterns = [
    path('patients', PatientsView.as_view()),
    path('visits',VisitsView.as_view()),
    path('symptoms',SymptomsView.as_view()),
    path('prescriptions',PrescriptionsView.as_view()),
]
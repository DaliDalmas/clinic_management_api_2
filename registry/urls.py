from django.urls import path
from .views import PatientsView

urlpatterns = [
    path('patients', PatientsView.as_view()),

]
from django.urls import path, include
from .views import RegistrationView

urlpatterns = [
    path('register',RegistrationView.as_view())
]

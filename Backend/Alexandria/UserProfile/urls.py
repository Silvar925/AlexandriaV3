from django.urls import path
from .views import authentication, registration_view

urlpatternsUserProfile = [
    path('authentication/', authentication, name="authentication"),
    path('registration', registration_view, name="registration")
]
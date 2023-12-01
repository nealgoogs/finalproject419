# SurveyLanding/urls.py
from django.urls import path
from .views import landing_page, redirect_based_on_entries

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('start/', redirect_based_on_entries, name='redirect_base_on_entries'),
]

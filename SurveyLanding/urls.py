# SurveyLanding/urls.py
from django.urls import path
from .views import landing_page, redirect_randomly

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('start/', redirect_randomly, name='redirect_randomly'),
]

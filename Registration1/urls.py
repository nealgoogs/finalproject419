from django.urls import path
from .views import register, survey, thankyou

app_name = 'Registration1'

urlpatterns = [
    path('register/', register, name='registration1_register'),
    path('survey/', survey, name='registration1_survey'),
    path('thankyou/', thankyou, name='thank_you'),
]

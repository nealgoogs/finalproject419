from django.urls import path
from .views import register, thankyou, survey

app_name = 'Register2'

urlpatterns = [
    path('register/', register, name='registration2_register'),
    path('survey/', survey, name='registration2_survey'),
    path('thankyou/', thankyou, name='registration1_thankyou'),
]
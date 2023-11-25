from django.urls import path
from .views import register, thankyou

app_name = 'Registration1'

urlpatterns = [
    path('register/', register, name='registration1_register'),
    path('thankyou/', thankyou, name='registration1_thankyou'),
]

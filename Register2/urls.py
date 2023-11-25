from django.urls import path
from .views import register, thankyou

app_name = 'Register2'

urlpatterns = [
    path('register/', register, name='registration2_register'),
    path('thankyou/', thankyou, name='registration1_thankyou'),
]
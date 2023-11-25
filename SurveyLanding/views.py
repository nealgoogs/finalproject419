
import random
from django.shortcuts import render, redirect

def landing_page(request):
    return render(request, 'landing_page.html')

def redirect_randomly(request):
    registration_pages = ['Registration1:registration1_register', 'Register2:registration2_register', 'Register3:registration3_register']
    return redirect(random.choice(registration_pages))

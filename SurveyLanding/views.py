from Registration1.models import UserCredentials1
from Register2.models import UserCredentials2
from Register3.models import UserCredentials3
from django.shortcuts import render, redirect

def landing_page(request):
    return render(request, 'landing_page.html')

def redirect_based_on_entries(request):
    # Count entries in each database
    count1 = UserCredentials1.objects.count()
    count2 = UserCredentials2.objects.count()
    count3 = UserCredentials3.objects.count()

    # Determine which form to prioritize
    min_count, form_to_redirect = min(
        (count1, 'Registration1:registration1_register'),
        (count2, 'Register2:registration2_register'),
        (count3, 'Register3:registration3_register')
    )

    # Redirect to the form with the least entries
    return redirect(form_to_redirect)

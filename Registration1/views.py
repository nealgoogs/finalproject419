from django.shortcuts import render, redirect
from .forms import UserRegistrationForm1
from zxcvbn import zxcvbn

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm1(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password_strength_result = zxcvbn(form.cleaned_data['password'])  # Correct usage
            user.password_strength = password_strength_result['score']
            user.save()
            return redirect('registration1_thankyou')
    else:
        form = UserRegistrationForm1()
    return render(request, 'register.html', {'form': form})



def thankyou(request):
    return render(request, 'thankyou.html')
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm3
from zxcvbn import zxcvbn  # Correct import statement

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm3(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password_strength_result = zxcvbn(form.cleaned_data['password'])  # Correct usage
            user.password_strength = password_strength_result['score']
            user.save()
            return redirect('Registration1:registration1_thankyou')
    else:
        form = UserRegistrationForm3()
    return render(request, 'register3.html', {'form': form})



def thankyou(request):
    return render(request, 'thankyou.html')
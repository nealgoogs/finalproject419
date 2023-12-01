from django.shortcuts import render, redirect
from .forms import UserRegistrationForm1
from zxcvbn import zxcvbn
from .forms import SurveyForm
from .models import UserCredentials1


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm1(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password_strength_result = zxcvbn(form.cleaned_data['password'])  # Correct usage
            user.password_strength = password_strength_result['score']
            user.save()
            request.session['user_id'] = user.id
            return redirect('Registration1:registration1_survey')
    else:
        form = UserRegistrationForm1()
    return render(request, 'register.html', {'form': form})



def survey(request):

    user_id = request.session.get('user_id')  # Retrieve the user ID
    user = UserCredentials1.objects.get(id=user_id)

    if request.method == "POST":
        form = SurveyForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('Registration1:thank_you')
    else:
        form = SurveyForm(instance=user)

    return render(request, 'survey.html', {'form': form})

def thankyou(request):
    return render(request, 'thankyou.html')
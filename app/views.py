from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserLoginForm
from app.models import CustomUser, CustomUserManager

from django.contrib.auth import authenticate, login, logout


# Create your views here.

def homepage(request):

	context = {}

	return render (request, 'base.html', context)


def login_view(request):  
    context = {}

    context['form'] = CustomUserLoginForm()

    if request.method == 'POST':

        form = CustomUserLoginForm(request.POST)
        context['form'] = form

        if form.is_valid():
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password', None)

            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
            except Exception, e:
                message = """
                username or password incorrect, try again
                <a href='/login/'>login<a>
                """
                return HttpResponse(message)

    return render(request, 'signin.html', context)


def sign_up(request):

    context = {}

    context['form'] = CustomUserCreationForm()

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password1', None)

            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
            except Exception, e:
                print e
                return HttpResponse('invalid user or password, try again <a href="/signup/">here</a>')

    return render(request, 'signup.html', context)



def logout_view(request):  
    logout(request)

    return redirect('/signup/')



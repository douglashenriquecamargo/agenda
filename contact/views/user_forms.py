from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm

from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()
    
    context = {
        "form": form,
        "title": "Register"
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário registrado com sucesso")
            return redirect('contact:index')
    
    return render(request, 'contact/register.html', context)


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)

    context = {
        "form": form,
        "title": "Login"
    }

    return render(request, 'contact/login.html', context)


def logout_view(request):
    auth.login(request)
    return redirect('contact:login', request.user)

"""Views for the accounts app"""
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm


def signup(request):
    """View for the signup page
    :param request: incoming http request
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

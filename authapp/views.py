from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Views
@login_required
def index(request):
    return render(request, "registration/home.html", {})


def register(request):
    """
    Handle user registration.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: Rendered registration page or redirect to home page on successful registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('authapp:home')
    else:
        # Display an empty registration form for GET requests
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
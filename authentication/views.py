from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST.get('username', ''), password=request.POST.get('password', ''))
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', '/'))
            else:
                messages.error(request, 'No account matched with that username and password')
    else:
        form = AuthenticationForm(None)

    return render(request, 'login.html', { 'form' : form })

def signout(request):
    logout(request)
    return redirect('/')
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import CustomUserForm, LoginForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.



# view pour s'enregitrer:
def user_registration(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:homepage')
    else:
        form = CustomUserForm()
    ctx = {'form':form}
    return render(request, 'authenticate/registration.html', ctx)



# view pour se login:
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            my_username = form.cleaned_data['my_username']
            my_password = form.cleaned_data['my_password']
            user = authenticate(
                request,
                password = my_password,
                username = my_username
            )
            if user is not None:
                login(request, user)
                # gestion du next pour le mixin
                if request.GET.get('next'):
                    new_url = request.GET.get('next')
                    return redirect(new_url)
                return redirect('home:homepage')
            else:
                form.add_error(None, 'Identifiant ou mot de passe invalide !')

    else:
        form = LoginForm()

    ctx = {'form':form}
    return render(request, 'authenticate/login_page.html', ctx)

# view pour se logout :
def logout_page(request):
    logout(request)
    return redirect('home:homepage')
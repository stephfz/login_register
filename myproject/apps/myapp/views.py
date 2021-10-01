from django.shortcuts import render, redirect   

from .forms.customForms import LoginForm
from .forms.user import UserForm

def index(request):
    return render(request, 'index.html')

def logout(request):
    try:
        del request.session['logged_username']
    except:
        print('Error')
    return redirect('/')      

def login(request):
    formLogin = LoginForm(request.POST or None)
    if request.method == "POST":
        if formLogin.is_valid():
            logged_user = formLogin.login()
            if logged_user != None:
                request.session['logged_username'] = logged_user.name
                return redirect('/home')      
    return render(request, 'login.html', {'formLogin':formLogin})

def register(request):
    formRegister = UserForm(request.POST or None)
    if request.method == "POST":
        if formRegister.is_valid():
            new_user = formRegister.save()
            request.session['logged_username'] = new_user.name
            return redirect('/home')
    return render(request, 'register.html', {'formRegister': formRegister})    

def home(request):
    return render(request,'home.html')    

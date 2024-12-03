from django.shortcuts import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def Home(Request):
    current_page = 'home'
    return render(Request,"index.html",{ 'current_page': current_page})



def logout_view(request):
    logout(request)
    return redirect(Home)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'User Name or Password Incorrect.'
    else:
        error = None
    return render(request, 'admin/admin-login.html', {'error': error})

def gallery(request):
    current_page = 'gallery'
    return render(request,'gallery.html', { 'current_page': current_page})


def about(request):
    current_page = 'about'
    return render(request,'about.html', { 'current_page': current_page})

def event(request):
    current_page = 'event'
    return render(request,'event.html', { 'current_page': current_page})
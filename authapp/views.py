from django.shortcuts import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def Home(Request):
    return render(Request,"index.html")



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
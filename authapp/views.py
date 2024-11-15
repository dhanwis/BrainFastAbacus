from django.shortcuts import *
from django.contrib.auth import logout
def Home(Request):
    return render(Request,"index.html")

def dashboard(Request):
    return render(Request,'admin/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('Home')
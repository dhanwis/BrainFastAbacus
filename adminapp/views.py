from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/admin/login/')  
def dashboard(Request):
    return render(Request,'admin/dashboard.html')
from django.shortcuts import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from adminapp.models import*
from django.core.paginator import Paginator


def Home(Request):
    current_page = 'home'
    events = Event.objects.all().order_by('-id')[:3]
    newss=News.objects.all()
    context = {
        'events': events,
        'newss':newss,
        'current_page':current_page
        
    }
    return render(Request,"index.html",context)



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
    events = Gallery.objects.all().order_by('-id')  # Fetch events in descending order of creation
    paginator = Paginator(events, 9)  # 9 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   

    context = {
        'page_obj': page_obj,
        'current_page':current_page
        
    }
    return render(request, 'gallery.html', context)


def about(request):
    current_page = 'about'
    return render(request,'about.html', { 'current_page': current_page})

def event(request):
    current_page = 'event'
    events = Event.objects.all().order_by('-id') # Fetch events in descending order of creation
    paginator = Paginator(events, 9)  # 9 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   

    context = {
        'page_obj': page_obj,
        'current_page':current_page
        
    }
    return render(request, 'event.html', context)

def contact(request):
    current_page='contact'
    return render(request,'contact.html',{'current_page':current_page})

def abacuscourse(request):
    current_page='abacuscourse'
    return render(request,'abacuscourse.html',{'current_page':current_page})


def vedicmath(request):
    current_page='vedicmath'
    return render(request,'vedicmath.html',{'current_page':current_page})

def abacusttc(request):
    current_page='abacusttc'
    return render(request,'abacusttc.html',{'current_page':current_page})

def vedictcc(request):
    current_page='vedicttc'
    return render(request,'vedicttc.html',{'current_page':current_page})
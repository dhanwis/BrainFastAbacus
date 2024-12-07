from django.shortcuts import*
from django.contrib.auth.decorators import login_required
from .models import*
from django.contrib import messages 
# Create your views here.

@login_required(login_url='/admin/login/')  
def dashboard(Request):
    current_page = 'dashboard'
    return render(Request,'admin/dashboard.html', { 'current_page': current_page})

@login_required(login_url='/admin/login/')
def image_add(request):
    current_page = 'imageadd'
    if request.method == 'POST':
        image = request.FILES.get('image') 
        try:
            gallery= Gallery(image=image)
            gallery.save()
            messages.success(request, 'image added successfully')
            return redirect('imagelist')
        except Exception as e:
            messages.error(request, f'Error adding image: {e}')
            return redirect('image_add')
        
    context = {
        'current_page': current_page,
    } 
    return render(request, 'admin/imageadd.html', context)


@login_required(login_url='/admin/login/')    
def image_list(request):
    current_page = 'imagelist'
    gallerys = Gallery.objects.all()
    context = {
        'current_page': current_page,
        'gallerys': gallerys
        }
    return render(request, 'admin/imagelist.html',context)


@login_required(login_url='/admin/login/')
def image_view(request, image_id):
    current_page = 'imageview'
    try:
        gallery = Gallery.objects.get(id=image_id)
    except gallery.DoesNotExist:
        messages.error(request, 'image not found')
        return redirect(image_list)
    context = {
        'current_page': current_page,
        'gallery':gallery
    }
    return render(request, 'admin/imageview.html', context)
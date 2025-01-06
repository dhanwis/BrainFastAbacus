from django.shortcuts import*
from django.contrib.auth.decorators import login_required
from .models import*
from django.contrib import messages 
# Create your views here.

@login_required(login_url='/admin/login/')  
def dashboard(Request):
    image_count = Gallery.objects.count()
    event_count = Event.objects.count()
    news_count=News.objects.count()
    current_page = 'dashboard'
    context = {
        'current_page': current_page,
        'image_count':image_count,
        'event_count':event_count,
        'news_count':news_count
    } 
    
    return render(Request,'admin/dashboard.html', context)

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

@login_required(login_url='/admin/login/')
def event_add(request):
    current_page = 'eventadd'
    if request.method == 'POST':
        image = request.FILES.get('image') 
        description = request.POST.get('description')
        try:
            event= Event(image=image,description=description)
            event.save()
            messages.success(request, 'event added successfully')
            return redirect('eventlist')
        except Exception as e:
            messages.error(request, f'Error adding event: {e}')
            return redirect('eventadd')
        
    context = {
        'current_page': current_page,
    } 
    return render(request, 'admin/eventadd.html', context)

@login_required(login_url='/admin/login/')    
def event_list(request):
    current_page = 'eventlist'
    events = Event.objects.all()
    context = {
        'current_page': current_page,
        'events': events
        }
    return render(request, 'admin/eventlist.html',context)

@login_required(login_url='/admin/login/')    
def image_edit(request, image_id):
    current_page = 'imageedit'
    try:
        gallery = Gallery.objects.get(id=image_id)
    except Gallery.DoesNotExist:
        messages.error(request, 'image not found')
        return redirect('imagelist')

    if request.method == 'POST':
        try:
            image = request.FILES.get('image')
              # Update the image field
            if image:
                gallery.image = image

            gallery.save()
            messages.success(request, 'image edited successfully')
            return redirect('imagelist')
        except Exception as e:
            messages.error(request, f'Error editing image: {e}')
            return redirect('imageedit', image_id=gallery.id) 

    context = {
        'current_page': current_page,
        'gallery': gallery
        }
    return render(request, 'admin/editimage.html', context)

@login_required(login_url='/admin/login/')   
def event_edit(request, event_id):
    current_page = 'window_edit'
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        messages.error(request, 'event not found')
        return redirect('eventlist')

    if request.method == 'POST':
        try:
            image = request.FILES.get('image')
            event.description = request.POST.get('description')
            

            # Update the image field
            if image:
                event.image = image

            event.save()
            messages.success(request, 'event edited successfully')
            return redirect('eventlist')
        except Exception as e:
            messages.error(request, f'Error editing event: {e}')
            return redirect('window_edit', event_id=event.id) 

    context = {
        'current_page': current_page,
        'event': event
        }
    return render(request, 'admin/eventedit.html', context)


@login_required(login_url='/admin/login/')
def event_view(request, event_id):
    current_page = 'eventview'
    try:
        event = Event.objects.get(id=event_id)
    except event.DoesNotExist:
        messages.error(request, 'image not found')
        return redirect(image_list)
    context = {
        'current_page': current_page,
        'event':event
    }
    return render(request, 'admin/eventview.html', context)

@login_required(login_url='/admin/login/')
def image_delete(request, image_id):
    try:
        gallery = Gallery.objects.get(id=image_id)
    except Gallery.DoesNotExist:
        messages.error(request, 'image not found')
        return redirect('imagelist')
    
    try: 
        gallery.delete()
        messages.success(request, 'image deleted successfully')
        return redirect('imagelist')
    except Exception as e:
        messages.error(request, f'Error deleting gallery: {e}')
        return redirect('imagelist')
    
    
@login_required(login_url='/admin/login/')    
def event_delete(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        messages.error(request, 'event not found')
        return redirect('eventlist')
    
    try: 
        event.delete()
        messages.success(request, 'event deleted successfully')
        return redirect('eventlist')
    except Exception as e:
        messages.error(request, f'event deleting gallery: {e}')
        return redirect('eventlist')
    
    
@login_required(login_url='/admin/login/')
def news_add(request):
    current_page = 'newsadd'
    if request.method == 'POST':
        description = request.POST.get('description')
        try:
            news = News(description=description)  # Save description and image
            news.save()
            messages.success(request, 'News added successfully')
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f'Error adding news: {e}')
            return redirect('newsadd')

    context = {
        'current_page': current_page,
    }
    return render(request, 'admin/Addnewsdescription.html', context)

@login_required(login_url='/admin/login/')    
def news_list(request):
    current_page = 'newslist'
    newss = News.objects.all()
    context = {
        'current_page': current_page,
        'newss': newss
        }
    return render(request, 'admin/newslist.html',context)


@login_required(login_url='/admin/login/')
def news_edit(request, news_id):
    current_page = 'newsedit'
    try:
        news = News.objects.get(id=news_id)
    except News.DoesNotExist:
        messages.error(request, 'News not found')
        return redirect('newslist')

    if request.method == 'POST':
        try:
            news.description = request.POST.get('description')
            news.save()
            messages.success(request, 'News edited successfully')
            return redirect('newslist')
        except Exception as e:
            messages.error(request, f'Error editing news: {e}')
            return redirect('newsedit', news_id=news.id)

    context = {
        'current_page': current_page,
        'news': news
    }
    return render(request, 'admin/newsedit.html', context)


    
@login_required(login_url='/admin/login/')    
def news_delete(request, news_id):
    try:
        news= News.objects.get(id=news_id)
    except News.DoesNotExist:
        messages.error(request, 'news not found')
        return redirect('newslist')
    
    try: 
        news.delete()
        messages.success(request, 'news deleted successfully')
        return redirect('newslist')
    except Exception as e:
        messages.error(request, f'error deleting news: {e}')
        return redirect('newslist')
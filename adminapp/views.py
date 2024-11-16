from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/admin/login/')  
def dashboard(Request):
    return render(Request,'admin/dashboard.html')

@login_required(login_url='/admin/login/')
def image_add(request):
    current_page = 'imageadd'
    # if request.method == 'POST':
    #     image = request.FILES.get('image') 
    #     head = request.POST.get('head')
    #     description = request.POST.get('description')
        
    #     try:
    #         door = Door(
    #             image=image,
    #             head=head,
    #             description=description,
    #         )
    #         door.save()
    #         messages.success(request, 'door added successfully')
    #         return redirect('door_list')
    #     except Exception as e:
    #         messages.error(request, f'Error adding door: {e}')
    #         return redirect('door_add')
        
    context = {
        'current_page': current_page,
    } 
    return render(request, 'admin/imageadd.html', context)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Thread,Notification
from cars.models import UsedCars
from accounts.models import User
from django.db.models import Q
# Create your views here.

def create_thread(user,car_owner):
    thread = Thread(first_person = user,second_person = car_owner)    
    thread.save()
    
    
def chatroom(request):
    search = request.GET.get('Search','')
    user = request.user
    threads = Thread.objects.by_user(user = user).prefetch_related('chatmessage_thread').order_by('timestamp')
    if search:
        threads = Thread.objects.filter(
             Q(second_person__first_name__icontains = search, first_person__first_name = user.first_name)|
             Q(first_person__first_name__icontains = search, second_person__first_name = user.first_name)
             )
    
    if not threads.exists():
       
        car_id = request.GET.get('car_id','')
        
        car = UsedCars.objects.get(id = car_id)
       
        car_owner = car.user
     
        thread = create_thread(user,car_owner)
       
    context = {
        'Threads': threads,
        'search':search
    }
    return render (request,'chat/messages.html',context)



@login_required
def notification_count(request):
    dumps = []
    notifications = request.user.notifications.filter()
    count = request.user.notifications.filter(is_read=False).count()
    for notification in notifications:
            print(notification.sender.first_name)
            data = {
                'user_name':notification.sender.first_name, 
                'notification_id':notification.id,
                'is_read':notification.is_read, 
            }
            dumps.append(data)
    return JsonResponse(
         {'notifications':dumps,
          'unread_count': count}
          )

def update_notification(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'GET':
        id  = request.GET.get('id')
        notifications = Notification.objects.get(id = id)
        notifications.is_read = True
        notifications.save()
        return JsonResponse({'success':True})
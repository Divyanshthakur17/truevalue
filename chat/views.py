from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404

from .models import Thread
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
    print(user.first_name)
    threads = Thread.objects.by_user(user = user).prefetch_related('chatmessage_thread').order_by('timestamp')
    if search:
        print('@@@@@@@@@@@@@')
        threads = Thread.objects.filter(Q(second_person__first_name__icontains = search, first_person__first_name = user.first_name)|Q(first_person__first_name__icontains = search, second_person__first_name = user.first_name))
    
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
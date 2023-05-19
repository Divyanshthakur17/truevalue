from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Thread
from cars.models import UsedCars

# Create your views here.

@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user = request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    print(threads)
    context = {
        'Threads': threads
    }
    return render(request, 'chat/messages.html', context)

def send_msg(request,pk):
    car_user = UsedCars.objects.get(pk=pk)
    print(car_user.user)
    return render(request,'chat/messages.html')
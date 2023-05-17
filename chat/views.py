from django.shortcuts import render

# Create your views here.
def messages_page(request):
    context = {

    }
    return render(request, 'chat/messages.html', context)
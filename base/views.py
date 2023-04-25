from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'base/index.html')


def about(request):
    return render(request,'base/about.html')


def agents(request):
    return render(request,'base/agents.html')

def blogs(request):
    return render(request,'base/blogs.html')

def contact(request):
    return render(request,'base/contact.html')




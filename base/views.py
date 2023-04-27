from django.shortcuts import render
from .models import Agents, Blog, About,Contact
from cars.models import NewCars,UsedCars
# Create your views here.
def index(request):
    cars = NewCars.objects.all()
    usedcars = UsedCars.objects.all()
    about = About.objects.get(id=1)
    return render(request,'base/index.html',{"cars":cars,"usedcars":usedcars, "about":about} )


def about(request):
    about = About.objects.get(id=1)
    return render(request,'base/about.html', {"about":about})


def agents(request):
    agents = Agents.objects.all()
    return render(request,'base/agents.html',{'agents':agents})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request,'base/blogs.html',{"blogs":blogs})

def contact(request): 
    print(request.POST)
    if request.method == 'POST':
        print("________")
        full_name = request.POST['full_name']
        email = request.POST['email']
        contact = request.POST['contact']
        print("____________")
        message = request.POST['message']
        contact = Contact(full_name=full_name,email=email,contact=contact,message=message) 
        contact.save()
    return render(request,'base/contact.html')




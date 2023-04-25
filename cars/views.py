from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import NewCars, UsedCars


# Create your views here.
def NewCarViews(request):
    # for sort filter
    ordering = request.GET.get('ordering', "")
    cars = NewCars.objects.all()
    
    if ordering:
        cars = cars.order_by(ordering)

    # for pagination
    page_number = request.GET.get('page', 1)
    
    p = Paginator(cars,2)
    page_number = request.GET.get('page')
    try:
        cars = p.page(page_number)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        cars = p.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        cars = p.page(p.num_pages)
    context = {"cars": cars, "page_obj": cars}
    return render(request, "base/newcars.html", context)

def UsedCarViews(request):
    # for sort filter
    ordering = request.GET.get('ordering', "")
    cars = UsedCars.objects.all()
    if ordering:
        cars = cars.order_by(ordering)
        
    page_number = request.GET.get('page', 1)
    
    p = Paginator(cars,3)
    page_number = request.GET.get('page')
    try:
        cars = p.page(page_number)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        cars = p.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        cars = p.page(p.num_pages)
    context = {"cars": cars, "page_obj": cars}
    return render(request, "base/usedcars.html", context)


def cardetail(request,pk):
    detail = get_object_or_404(NewCars,pk = pk)
    return render(request,'base/details.html',{'car':detail})

def usedcardetail(request,pk):
    detail = get_object_or_404(UsedCars,pk = pk)
    return render(request,'base/olddetails.html',{'car':detail})


def high_low(request):
    cars = NewCars.objects.all().order_by('-exshowroom_price')
    return render(request,'base/newcars.html',{'cars':cars})
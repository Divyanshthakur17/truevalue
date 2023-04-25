from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import NewCars, UsedCars


# Create your views here.
def NewCarViews(request):
    # for sort filter
    ordering = request.GET.get('ordering', "")
    exshowroom_price = request.GET.get('exshowroom_price', "")
    body_type = request.GET.get('body_type', "")
    milege = request.GET.get('milege', "")
    cars = NewCars.objects.all()
    
    if ordering:
        cars = cars.order_by(ordering)
        print(cars)

    if exshowroom_price:
        cars = cars.filter(exshowroom_price__lt = exshowroom_price)

    if body_type:
        cars = cars.filter(body_type = body_type)

    if milege:
        cars = cars.filter(milege__lt = milege)
        print(cars)
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
    price = request.GET.get('price', "")
    kilometer_run = request.GET.get('kilometer_run', "")
    buy_year = request.GET.get('buy_year', "")
  
    cars = UsedCars.objects.all()
    if ordering:
        cars = cars.order_by(ordering)
    
    if price:
        cars = cars.filter(demand__lt = price)
        
    if kilometer_run:
        cars = cars.filter(kilometer_run__lt = kilometer_run)

    if buy_year:
        cars = cars.filter(buy_year = buy_year)
        
    
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
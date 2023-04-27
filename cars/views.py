from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import NewCars, UsedCars
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q


# Create your views here.
def NewCarViews(request):
    # for sort filter
    ordering = request.GET.get('ordering', "")
    price = request.GET.get('price', "")
    body_type = request.GET.get('body_type', "")
    milege = request.GET.get('milege', "")
    search = request.GET.get('search', "")

    cars = NewCars.objects.all()

    if search:
        cars = NewCars.objects.filter(Q(car_name__icontains=search) | Q(body_type__icontains=search) | Q(color__icontains=search)) 

    
    if ordering:
        cars = cars.order_by(ordering)
        

    if price:
        cars = cars.filter(exshowroom_price__lt = price)

    if body_type:
        cars = cars.filter(body_type = body_type)

    if milege:
        cars = cars.filter(milege__lt = milege)
        
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

    if (request.GET.get('mybtn')):
        print(f'THIS IS THE TEXT VALUE: {search}')
    else:
        print('Has not been clicked')
    
        
    context = {"cars": cars, "page_obj": cars, "search":search,"body_type":body_type,"milege":milege, "price":price, "ordering":ordering}
    return render(request, "base/newcars.html", context)











def UsedCarViews(request):
    # for sort filter
    search = request.GET.get('usedsearch', "")
    ordering = request.GET.get('ordering', "")
    price = request.GET.get('price', "")
    kilometer_run = request.GET.get('kilometer_run', "")
    buy_year = request.GET.get('buy_year', "")
  
    cars = UsedCars.objects.all()

    if search:
        cars = UsedCars.objects.filter(Q(usedcar_name__icontains=search) | Q(fuel_type__icontains=search)) 

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



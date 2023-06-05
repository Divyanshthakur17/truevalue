from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.urls import reverse
from .models import NewCars, UsedCars,Commentcars, Cart,WishItem, Brand , Model,State, Cities
from django.http import JsonResponse,HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from .forms import CarCommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
import json
from django.http import HttpRequest

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
    
        
    context = {
        "cars": cars, 
        "page_obj": cars, 
        "search":search,
        "body_type":body_type,
        "milege":milege, 
        "price":price, 
        "ordering":ordering
        }
    return render(request, "cars/newcars.html", context)











def UsedCarViews(request):
    cars = UsedCars.objects.filter()
    ordering = request.GET.get('ordering', "")
    if ordering:
            cars = cars.order_by(ordering)
        
    states = State.objects.all()
    
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'GET':
        print('ajax-------------------------')
    # if request.headers.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest" and request.method == 'GET':
        print('ajax-------------------------')
        search = request.GET.get('usedsearch', "")
        
        price = request.GET.get('price', "")
        city = request.GET.get('cities', "")
        state = request.GET.get('states', "")
  
        dumps = []
        
    


        if search:
            cars = UsedCars.objects.filter(Q(usedcar_name__icontains=search) | Q(fuel_type__icontains=search)) 

        
        if price:
            cars = cars.filter(demand__lt = price)
            
        if city:
            cars = cars.filter(cities__cities = city)

        if state:
            cars = cars.filter(states__states = state)
            # print(cars,"-----------------------------")
        
        # cars = cars.values('')
        # context = {
        #     'search':search,
        #     'price':price,
        #     'city':city,
        #     'state':state,
        #     'cars':cars
        # }
        for car in cars:
        #     br = Brand.objects.get(id=car.brand_id).brand_desc
        #     setattr(car,"brandname",br)
        #     print(car.brandname)
        # print(cars[0].brandname)    
        # print(cars.values())
        # cars = cars.values()
            data = {
                'brand_name':car.brand.brand_name,
                'image_1':str(car.image_1),
                'demand':car.demand,
                'model':car.model.model_name,
                'first_name':car.user.first_name,
                'car_id':car.id,
                'user':str(car.user),
                'logged_user':str(request.user)
                # 'cars':list(cars),
                # 'page_obj':list(cars),
            }
            dumps.append(data)
            context = {'cars':dumps}
        
        return JsonResponse(context)
        # return HttpResponse(json.dumps({"cars":carss}))
    page_number = request.GET.get('page', 1)
    
    p = Paginator(cars,1)
    page_number = request.GET.get('page')
    try:
        cars = p.page(page_number)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        cars = p.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        cars = p.page(p.num_pages)
    

    context = {
        "cars": cars,
        "page_obj": cars,
        'ordering':ordering,
        'states':states
    }
    return render(request, "cars/usedcars.html", context)




def cardetail(request,pk):
    detail = get_object_or_404(NewCars,pk = pk)
    return render(request,'cars/details.html',{'car':detail})


global_car_id = 0

def usedcardetail(request,pk):
    global global_car_id
    global_car_id = int(pk)
    print(global_car_id)
    car = get_object_or_404(UsedCars,pk = pk)
    comments = Commentcars.objects.filter(usedcar=car)
    if request.method == "POST":
        comment_form = CarCommentForm(data=request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.usedcar = car
            comment.save()
    else:
        comment_form = CarCommentForm()
    return render(request,'cars/olddetails.html',{'car':car,"comments":comments, "comment_form":comment_form})


def cartview(request):
    user = request.user
    if user.is_authenticated:
        cart =  Cart.objects.filter(user=user.id )
        print(cart)

        
        context = {
            "carts":cart
        }
        return render(request,"cars/addtocart.html",context)

def wishlist(request):
    current_user = request.user
    print(current_user)
    if current_user.is_authenticated:
        cars = WishItem.objects.get(user=current_user).cars.all()
        context ={
            'user': current_user,
            "cars":cars
        }
        return render(request,"cars/wishlist.html", context)
    


def addToWishlist(request):
    if request.method == "POST":
        print(request.POST)
        car_id = request.POST.get('car-id')
        print(car_id)
        
        car = UsedCars.objects.get(id= car_id)
        print(car)
        s = WishItem.objects.get(user=request.user)
        s.cars.add(car)
        return HttpResponseRedirect(reverse('usedcars'))


def deleteFromWishlist(request):
    if request.method == "POST":
        car_id = request.POST.get('car_id')
        car = UsedCars.objects.get(id= car_id)
        s = WishItem.objects.get(user=request.user)
        s.cars.remove(car)
        print(car_id)     
        return HttpResponseRedirect(reverse('wishlist'))

def addCars(request):
    brands = Brand.objects.all()
    models = Model.objects.all()

    if request.method == 'POST':
        if "image_1" in request.FILES:
            image_1 = request.FILES['image_1']
        if "image_2" in request.FILES:
            image_2 = request.FILES['image_2']
        if "image_3" in request.FILES:
            image_3 = request.FILES['image_3']
            image_3=image_3
        if "image_4" in request.FILES:
            image_4 = request.FILES['image_4']
            image_4=image_4
        if "image_5" in request.FILES:
            image_5 = request.FILES['image_5']
            image_5=image_5
        if "image_6" in request.FILES:
            image_6 = request.FILES['image_6']
            image_6=image_6
        carname = request.POST.get('carname')
     
        brand = request.POST.get('brand', "")
   
        brand = Brand.objects.get(brand_name = brand)
        
        model = request.POST.get('model', "")
       
        model = Model.objects.get(model_name = model)
        
   
        fuel_type = request.POST.get('fuel_type')
        milege = request.POST.get('milege')
        dent = request.POST.get('dent')
        kilometer_run = request.POST.get('kilometer_run')
        buy_year = request.POST.get('buy_year')
        demand = request.POST.get('demand')
        
        phone = request.POST.get('phone_no')
        car_desc = request.POST.get('car_desc')
        user = request.user

        if dent == 'on':
           dent = True
        else:
            dent = False

        car =UsedCars(image_1=image_1,image_2=image_2, usedcar_name=carname,brand=brand,model=model,user=user,fuel_type=fuel_type,milege=milege,dent=dent,kilometer_run=kilometer_run,buy_year=buy_year,demand=demand,phone_no=phone,used_car_detail=car_desc)
        car.save()
    context = {
        'brands':brands,
        "models":models
    }
    return render(request,'cars/addcars.html',context)


def load_models(request):
    brand_name = request.GET.get('brand')
    models = Model.objects.filter(brand__brand_name=brand_name).order_by('model_name')
    return render(request, 'cars/addcars_model_dropdown_list_options.html', {'models': models})

def load_cities(request):
    state_name = request.GET.get('states')
    print(state_name)
    cities = Cities.objects.filter(state__states=state_name).order_by('cities')
    print(cities)
    return render(request, 'cars/usedcars_model_dropdown.html', {'cities': cities})


# API for NewCars Model
from .serializers import NewCarsSerializer, UsedCarsSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission




class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        print('insidnde has permission', request.user)
        user = request.user
        if request.method == 'GET':
            return True

        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True

class UsedCarsViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    queryset = UsedCars.objects.all()
    serializer_class = UsedCarsSerializer

class NewCarsViewSets(ViewSet):
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    def list(self,request):
        cars = NewCars.objects.all()
        serializer = NewCarsSerializer(cars,many= True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = NewCarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self,request,pk):
        try:
            car = NewCars.objects.get(pk=pk)
        except NewCars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = NewCarsSerializer(car)
        return Response(serializer.data)
    
    def destroy(self,request,pk = None):
        try:
            car = NewCars.objects.get(pk=pk)
        except NewCars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class UsedCarsViewSets(ViewSet):
    def list(self,request):
        cars = UsedCars.objects.all()
        serializer = UsedCarsSerializer(cars,many= True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = NewCarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self,request,pk):
        try:
            car = NewCars.objects.get(pk=pk)
        except NewCars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = NewCarsSerializer(car)
        return Response(serializer.data)
    
    def destroy(self,request,pk = None):
        try:
            car = NewCars.objects.get(pk=pk)
        except NewCars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

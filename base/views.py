import os
from django.shortcuts import render, get_object_or_404,redirect, HttpResponseRedirect
from .models import Agents, Blog, About,Contact,Comment
from cars.models import NewCars,UsedCars
from . forms import CommentForm , ProfileImageForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.http import JsonResponse


# Create your views here.



def index(request):
    type = request.GET.get('type', "")
    search = request.GET.get('search', "")
    price = request.GET.get('price', "")
    body_type = request.GET.get('body_type', "")
   

    cars = NewCars.objects.all()
    usedcars = UsedCars.objects.all()
    about = About.objects.get(id=1)
    
    if type == "New":
        if search:
            cars = NewCars.objects.filter(Q(car_name__icontains=search) | Q(body_type__icontains=search) | Q(color__icontains=search)) 
        
        if price:
            cars = cars.filter(exshowroom_price__lt = price)

        if body_type:
            cars = cars.filter(body_type = body_type)

        return render(request,'cars/newcars.html', {"cars":cars,"search":search,"price":price,"Body Type": body_type})
    
    elif type == "Used":
        cars = usedcars
        print(cars)
        if search:
            cars = UsedCars.objects.filter(Q(usedcar_name__icontains=search)) 
        
        if price:
            cars = cars.filter(exshowroom_price__lt = price)

        if body_type:
            cars = cars.filter(body_type = body_type)
        print("-------##############--------")
        return render(request,'cars/usedcars.html', {"cars":cars,"search":search,"price":price,"Body Type": body_type})
    else:
        print("---------------")
        return render(request,'base/index.html',{"cars":cars,"usedcars":usedcars, "about":about} )



def about(request):
    about = About.objects.get(id=1)
    return render(request,'base/about.html', {"about":about})



def agents(request):
    agents = Agents.objects.all()
    return render(request,'base/agents.html',{'agents':agents})


def blogs(request):
    blogs = Blog.objects.all()
    # comment = request.GET.get('name', "")
    # blog_comment = Blog.objects.filter(comment=1)
    # print(blog_comment)
    return render(request,'base/blogs.html',{"blogs":blogs})



def blogdetail(request,pk):
    blog = get_object_or_404(Blog,pk = pk)
    comments = Comment.objects.filter(blog_id = blog, is_reply=False)
    comments_count = Comment.objects.filter(blog_id = blog, is_reply=False).count()


    user = request.user

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        print(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.is_reply = True
                    replay_comment.parent = parent_obj

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.user = user
            new_comment.blog = blog
            # Save the comment to the database
            new_comment.save()
            
            

            
    else:
        comment_form = CommentForm()

    context = {
        "blog":blog,
        'comments':comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comments_count':comments_count
    }
    return render(request,'base/blogdetail.html',context)




def contact(request): 
    if request.method == 'POST':
        print("________")
        full_name = request.POST['full_name']
        email = request.POST['email']
        contact = request.POST['contact']
        print("____________")
        message = request.POST['message']
        contact = Contact(full_name=full_name,email=email,contact=contact,message=message) 
        contact.save()
        context = {
            "success": True
        }
        return render(request,'base/contact.html',context)
    return render(request,'base/contact.html')

def user_profile_view(request):
    user = request.user
    print(user.id)
    image = User.objects.get(id = user.id)

    if user.is_authenticated:
        cars = UsedCars.objects.filter(user= user.id)
        form = ProfileImageForm()
        if request.method == 'POST':
            img = request.FILES.get('file')
            print(img,'___________________________')
       
            image.user_image = img
            image.save()
            # form.save()
            # return JsonResponse({'message': 'works'})    
            return redirect('user_profile')
        
        return render(request,"base/user_profile.html", {'cars':cars,"image":image,"form":form })
        
        # return render(request,"base/user_profile.html", {'cars':cars,"image":image,"form":form} )
    else:
        return redirect("signin ")
    

def edit_profile(request): 
    if request.user.is_authenticated:
        user = User.objects.get(email = request.user)
        # print(user.user_image)
        # print(len(str(user.user_image)))
        if request.method == 'POST':
            print('*********************************************')
            if "cover_image" in request.FILES:
                cover_image = request.FILES['cover_image']
                user.user_coverimage = cover_image
            if "user_image" in request.FILES:
                user_image = request.FILES['user_image']
                print('############################################3')
                print(user_image)
                user.user_image = user_image
                
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            
            
            
            
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.mobile = phone
            user.address = address
            user.save()
            return redirect('user_profile')

        context = {
            'user':user
        }
        return render(request,'base/editprofile.html',context)
    return render(request,'accounts/signin.html')


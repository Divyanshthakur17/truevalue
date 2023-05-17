from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from django.urls import reverse
from .forms import SignupForm 
from django.contrib.auth import get_user_model
from django.db.models.query_utils import Q
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from .helpus import Msghandler
import json
# Create your views here.
User = get_user_model()

def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('******')
            user = form.save()
            print(user)
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})

def sign_in(request):
    
    if request.method == "POST":
        resp = {'status':'failed'}
        username = request.POST["email"]
        password = request.POST["password"]
        try:
            new_user = User.objects.get(mobile = username)
            user = authenticate(username=new_user, password=password)
        except:
            user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            
            resp['status'] = 'success'

        else:
            resp['status'] = 'failed'
        return HttpResponse(json.dumps(resp),content_type = 'application/json')
    else:   
        return render(request, "accounts/signin.html")

def sign_out(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


global_var = 0

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        print(request.POST)
        global global_var
        
        otp = get_random_string(6, allowed_chars='123456789')
        global_var = int(otp)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            user = User.objects.get(email = data)
            mobile = user.mobile
            print(mobile)
            print(data)
            associated_users = User.objects.filter(Q(email=data))   
            if associated_users.exists():       
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset_email.txt"
                    mobile  = '+91'+ mobile
                    obj = Msghandler(mobile,otp)
                    obj.send_otp()
                    c = {
                        "otp":otp
                    }
                    email = render_to_string(email_template_name, c)
                    # response = fast2sms.requests.request('POST',url=fast2sms.url, data=fast2sms.payload , headers=fast2sms.headers)
                    print(email,"____________________________________")
                    # print(response)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    
                    context ={
                        "mail":data
                    }
                    
                    return render (request,'accounts/password_reset_done.html', context)
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})

global_mail = ''

def resetpassword(request):
    if request.method == "POST":
        data = request.POST.get('mail')
        print(data)
        global global_mail
        global_mail = data
 
        myotp = request.POST.get('otp')
        print(myotp)
        print(global_var)

        if myotp == str(global_var):
            print('######################')
            context ={
                        "mail":data
                    }
            return render(request,"accounts/password_reset_confirm.html",context)
        else:
            return redirect('password_reset_done')
        
    return render(request,"accounts/password_reset_confirm.html")

def resetpassword_complete(request):
    if request.method == "POST":
        mail = request.POST.get('mail')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')
        user = User.objects.get(email = mail)
        print(user)
        if pass1 == pass2:
            user.set_password(pass1)
            user.save()
            
            return render(request,"accounts/password_reset_complete.html")
        return redirect('password_reset_confirm')
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import F,Q

def register(request):
        if request.POST:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            #repeat=request.POST.get('confirm_password')

            if User.objects.filter(username=username,email=email).exists():
                #print("User already exists")
                messages.error(request, "already exists")
            else:
                user=user.objects.create_user(username=username,password=password,email=email)
                user.save()

            
                messages.success(request, "Registered successfully")
                return redirect('login/')  # Redirect to login page after successful registration
        
            

        return render(request,"registration.html")
def userlogin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        #email=request.POST['email']
        #email=request.POST['email']
        #print(username, "######################", password)
        user = authenticate(username=username, password=password,) # Retrieve the user object
        if user is not None:
            login(request,user)
           
            return redirect('update/')
         # Redirect to user profile page after successful login
    else:
        
        #print("Login Failed")
        messages.error(request, " login Failed")
        
    return render(request, 'login.html')
    

        


    
    
def update(request):
    if request.POST:
        bio=request.POST['bio']
        profile_picture=request.FILES['profile_picture']
        user=request.user
        user.userprofile.bio=bio
        user.userprofile.profile_picture=profile_picture
        #upqry=Userprofile.objects.create(bio=bio,pic=profile_picture)
        #upqry.save()
        user.userprofile.save()
        return redirect('update/')    

    return render(request,"update.html")

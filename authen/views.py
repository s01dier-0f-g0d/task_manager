from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        User.objects.create_user(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email=request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        messages.success(request,'Registration Successful')
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        customer = authenticate(request,
                                username = request.POST['username'],
                                password = request.POST['password']
        )
        if customer:
            login(request,customer)
            messages.success(request,'Login successful')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request,'signin.html')

@login_required(login_url='signin')
def profile(request):
    customer = request.user
    return render(request,'profile.html',{'customer':customer})

@login_required(login_url='signin')
def updatePass(request):
    if request.method == 'POST':
        customer = request.user
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if not customer.check_password(old_password):
            messages.error(request,'Wrong Old Password')
        elif old_password==new_password:
            messages.error(request,"New Password can't be same as Old Password")
        elif old_password!=new_password and new_password!=confirm_password:
            messages.error(request,'New Passowrd must be same as Confirm Password')
        else:
            customer.set_password(new_password)
            customer.save()
            update_session_auth_hash(request,customer)
            messages.success(request,'Password Changed')
            return redirect('profile')
    return render(request,'updatePass.html')

@login_required(login_url='signin')
def updateProfile(request):
    if request.method == 'POST':
        customer = request.user
        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.email = request.POST['email']
        customer.username = request.POST['username']
        customer.save()
        messages.success(request,'Profile Updated Successfully')
        return redirect('profile')
    return render(request,'updateProfile.html',{'customer':request.user})

@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('signin')
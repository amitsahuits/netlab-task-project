from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import signupform , userdetailForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == "POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            fm.save()
            print(request.user)
            messages.success(request,"YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY!!")
    else:
        fm = signupform()
    return render(request,'blog/signup.html', {'form':fm})

#user login
def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        print(request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request,'blog/login.html',{'form':fm})

#user profile
def profile(request):
    return render(request,'blog/profile.html',{'form':request.user})

#user detail
def userdetail(request):
    if request.method == "GET":
        fm = userdetailForm(instance=request.user)
        print('request.user :', request.user)
    else:
        if request.method == "POST":
            fm = userdetailForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'profile updated successfully.')
                fm.save()
        fm = userdetailForm(instance=request.user)
    return render(request, 'blog/userdetails.html', {'form': fm})

#user logout
def user_logout(request):
    logout(request)
    # this will redirect to login page after logout
    return HttpResponseRedirect('/')

#to see all other users list
#other users list only can seen by admin user , condition is applied on profile template
def userlist(request):
    alluser = User.objects.all()
    return render(request,'blog/userlist.html',{'userlist':alluser})

#to see other users details
#other user detail only can seen by admin user , condition is applied on profile template
def otheruser(request,id):
    otheruserdetails = User.objects.get(pk=id)
    return render(request, 'blog/otheruser.html', {'otheruserdetails': otheruserdetails})

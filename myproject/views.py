from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.db import IntegrityError
from django.db.models import Q 

# main nav Content
# -----------------------------------------------------------------------------



def base(req):

    return render (req, 'base.html')

def mybase(req):

    return render (req, 'mybase.html')

def home(req):

    return render (req, 'home.html')

def skills(req):

    return render (req, 'skills.html')

def experience(req):

    return render (req, 'experience.html')
def project(req):

    return render (req, 'project.html')

def blog(req):

    return render (req, 'blog.html')


def image_gallery(req):

    return render (req, 'image_gallery.html')

def one_gelary(req):
    data=photograph.objects.all()

    return render (req, '1nogelary.html', {"data":data})

def two_gelary(req):
    data=sports.objects.all()

    return render (req, '2nogelary.html', {"data":data})

def three_gelary(req):
    data=food.objects.all()

    return render (req, '3nogelary.html', {"data":data})

def four_gelary(req):
    data=work.objects.all()

    return render (req, '4nogelary.html', {"data":data})





# Authentication
# -----------------------------------------------------------------------------


def password_change(req):
    current_user=req.user
    if req.method == 'POST':
        currentpassword = req.POST.get("currentpassword")
        newpassword = req.POST.get("newpassword")
        confirmpassword = req.POST.get("confirmpassword")

        if check_password(currentpassword,req.user.password):
            if newpassword==confirmpassword:
                current_user.set_password(newpassword)
                current_user.save()
                update_session_auth_hash(req,current_user)
                return redirect("loginpage")
            
            
            if newpassword != confirmpassword:
                return redirect('password_change')
            else:
                return render(req, "password.html")
            
    return render(req, 'password.html')


def loginpage(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("password")

        # Check if both username and password are provided
        if not username or not password:
            return render(req, "login.html")

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect("base")
        else:
            return render(req, "login.html")

    return render(req, "login.html")


def registerpage(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        email = req.POST.get("email")
        user_type = req.POST.get("usertype")
        password = req.POST.get("password")
        confirm_password = req.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            return render(req, "signupPage.html")

        # Create user
        try:
            user = Custom_user.objects.create_user(
                username=username,
                email=email,
                user_type=user_type,
                password=password,
            )

            return redirect("loginpage")
        except IntegrityError:
            return render(req, "signupPage.html")

    return render(req, "signupPage.html")

def logoutpage(req):
    logout(req)
    return redirect('loginpage')





from django.shortcuts import render, redirect, get_object_or_404
from .models import rectify_profile

from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


import json
from django.views import View
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.user)
        if form.is_valid():
            rec_pro = form.save(commit=False)
            rec_pro.user = request.user
            rec_pro.save()
            upload = rectify_profile.objects.get(user=request.user)
            print(upload)
            context = {'posts': upload}
            return render(request, "profile.html", context)   
    else:
         upload = rectify_profile.objects.filter(user=request.user)
         if upload.exists():
            print(upload)
            print(upload[0])
            context = {'posts': upload[0]}
            return render(request, "profile.html", context)   
         else:
            form = ProfileForm()
            return render(request, 'profile.html' ,{'form':form})

def update(request):
    profile_edit = get_object_or_404(rectify_profile,user=request.user)
    form = ProfileForm(request.POST, instance=profile_edit)

    if form.is_valid():
        rec_pro = form.save(commit=False)
        rec_pro.user = request.user
        form.save()
        return redirect('profile')
    else:
        return render(request, 'edit.html', {'form':form})


    
# def edit(request, user_id):
#     edit = rectify_profile.objects.get(id=user_id)
#     if request.method == 'POST':


# def profile_new(request):
#     form = ProfileForm()
#     return render(request, "profile_new.html", {'form': form})

# def upload(request):
    
        # name = request.POST["name"]
        # email = request.POST["email"]
        # school = request.POST["school"]
        # contact = request.POST["contact"]
        # introduce = request.POST["introduce"]
        # rectify_profile.objects.create(name = name, email = email, school = school, contact = contact, introduce = introduce)
        # return redirect('profile')

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"] 
        cpassword = request.POST["cpassword"] 
        if password == cpassword:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["password"]
            )
            
            return render(request, "registration/login.html")
        else:
            err = "비밀번호가 다릅니다."
            context = {"err":err}
            return render(request, "registration/signup.html", context)
    else:
        return render(request, "registration/signup.html")

@login_required
def profile_edit(request, post):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            """
            현재 유저의 프로필을 가져오고
            받은 값으로 프로필을 갱신한다.
            """
            old_profile = rectify_profile.objects.get(user)
            old_profile.name = form.cleaned_data['name']
            old_profile.email = form.cleaned_data['email']
            old_profile.school = form.cleaned_data['school']
            old_profile.contact = form.cleaned_data['contact']
            old_profile.introduce = form.cleaned_data['introduce']
            old_profile.save()
            return redirect('profile')
    elif request.method == "GET":
        form = ProfileForm(instance=request.user.profile)
        return render(request, 'accounts/profile_form.html', {
            'form': form,
        })

def home(request):
    return render(request, 'home.html')
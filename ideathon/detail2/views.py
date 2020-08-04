from django.shortcuts import render, redirect
from .models import Post, Image
from .forms import Post_Form
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, "home.html")


def create_post(request):
    if request.method == "POST":
        post_form = Post_Form(request.POST, request.FILES)
        post_image = request.FILES.getlist("image")

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            for image in post_image:
                photo = Image(post = post, image = image)
                photo.save()
        
        # else:

    else:
        post_form = Post_Form()
        
    return redirect("detail_post")


def detail_post(request, pk):
    post = Post.objects.get(pk = pk)
    images = Image.objects.filter(post = post)
    context = {'post': post, 'images': images}
    return render(request, "detail.html", context)


def edit_post(request, pk):
    post = Post.objects.get(pk = pk)
    images = Image.objects.filter(post = post)

    if request.method == "POST":
        post.main_title = request.POST['main_title']
        post.sub_title = request.POST['sub_title']
        post.contents = request.POST['contents']
        post.user = request.user

        images.delete()

        post_image = request.FILES.getlist("image")

        for image in post_image:
            photo = Image(post = post, image = image)
            photo.save()

        post.save()
        return redirect("detail_post", pk=pk)
    else:
        context = {'post': post, 'image': images}
        return render(request, "post_edit.html", context)


def delete_post(request, pk):
    post = Post.objects.get(pk = pk)
    images = Image.objects.filter(post = post)
    images.delete()
    post.delete()

    return redirect("home")
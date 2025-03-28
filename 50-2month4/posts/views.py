from django.shortcuts import render ,redirect
from django.http import HttpResponse
import random
from posts.models import Post
from posts.forms import PostCreateform, PostCreateform2
from django.contrib.auth.decorators import login_required
def test_view(request):
    return HttpResponse(f"Hello, World ! {random.randint(1,100)}")


def home_page_view(request):
    if request.method == "GET":
        return render(request, "base.html")



@login_required(login_url="login")
def post_list_view(request):
    posts = Post.objects.all()
    if request.method == "GET":
        return render(request, "posts/post_list.html", {"posts": posts})

@login_required(login_url="login")
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail.html", {"post": post})

@login_required(login_url="login")
def post_create_view(request):
    if request.method == "GET":
        form = PostCreateform2()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostCreateform2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        elif form.is_valid():
            form.save()
         # title = form.cleaned_data["title"]
         # content = form.cleaned_data["content"]
         # image = form.cleaned_data["image"]
         # post = Post.objects.create(title=title, content=content, image=image)
        # if post:
            return redirect("post-list")





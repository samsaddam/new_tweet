from http.client import HTTPResponse
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import Post
from .forms import PostForm


def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # img = PostForm(request.FILES)
        # print(form)
    # If the form is valid
        if form.is_valid():
            # form.image = img
            # yes, save
            form.save()
          # Redirect to home
            return HttpResponseRedirect('/')

        else:
            # no, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm()
    # Show
    return render(request, 'posts.html', {'posts': posts})

def delete(request, post_id):
    # Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
    # Like post
    newlikecount = Post.objects.get(id = post_id)
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    # Edit post
    posts = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=posts)
        # img = PostForm(request.FILES)
        # print(form)
    # If the form is valid
        if form.is_valid():
            # form.image = img
            # yes, save
            form.save()
          # Redirect to home
            return HttpResponseRedirect('/')

        else:
            # no, Show Error
            return HttpResponseRedirect('not valid')
    return render(request, 'edit.html', {'posts': posts})

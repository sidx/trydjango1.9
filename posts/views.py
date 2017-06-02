# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Post
from .forms import PostForm

def post_list(request):
	# return HttpResponse("<h3>Hello</h3>")
	posts = Post.objects.all()
	context = {
	'page_title': 'List',
	'posts': posts
	}
	return render(request, 'base.html', context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		if request.method == 'POST':
			post_instance = form.save(commit=False)
		 	post_instance.save()
		 	return redirect('posts:list')
	context = {
		'form': form
	}
	return render(request, 'post_create.html', context)

def post_detail(request, id):
	post = get_object_or_404(Post, id=id)
	context = {
	'page_title':'Detail',
	'post': post
	}
	return render(request, 'post_detail.html', context)

def post_update(request, id=None):
	post = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=post)
	if form.is_valid and request.method == 'POST':
		post_instance = form.save(commit=False)
		post_instance.save()
		return HttpResponseRedirect('/posts/'+str(id))
	context = {
		'title': post.title,
		'post': post,
		'form': form,
	}
	return render(request, 'post_create.html', context)

def post_delete(request, id):
	post = get_object_or_404(Post, id=id)
	post.delete()
	return redirect("posts:list")
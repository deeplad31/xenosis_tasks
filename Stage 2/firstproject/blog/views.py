from django.shortcuts import render, get_list_or_404
from .models import BlogPost

def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_list_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post



# Create your views here.

def blog(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'blog/blog.html', context)


def add_post(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST.get('title')
        body = request.POST.get('body')
    
        Post.objects.create(author=author, title=title, body=body)
        return redirect('blog')
    return render(request, 'blog/add_post.html')


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        author = request.user
        title = request.POST.get('title')
        body = request.POST.get('body')
    
    return render(request, 'blog/edit_post.html', {'post':post})

from django.shortcuts import render, redirect
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
        print(title)
        Post.objects.create(author=author, title=title, body=body)
        return redirect('blog')
    return render(request, 'blog/add_post.html')


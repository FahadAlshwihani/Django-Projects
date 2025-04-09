from django.shortcuts import render, get_object_or_404
from .models import User, Post, Comment, Category

def main(request):
    return render(request, 'main.html')

def users(request):
    user_list = User.objects.all()
    return render(request, 'users.html', {'users': user_list})

def blogs(request):
    blog_list = Post.objects.all()
    return render(request, 'blogs.html', {'blogs': blog_list})

def comments(request):
    comment_list = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comment_list})

def categories(request):
    category_list = Category.objects.all()
    return render(request, 'categories.html', {'categories': category_list})

def blog_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blogdetails.html', {'post': post})
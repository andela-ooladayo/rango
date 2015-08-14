from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Category

# Create your views here.

def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, pk):
    return render_to_response('blog/view_post.html', {
        'post': get_object_or_404(Blog, pk=pk)
    })

def view_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render_to_response('blog/view_category.html',{
        'category' : category,
        'posts' : Blog.objects.filter(category=category)[:5]
    })
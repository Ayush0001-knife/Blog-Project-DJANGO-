from django.shortcuts import render
from .models import Categorie, Blogs
from django.http import HttpResponse

# Create your views here.
def posts_by_category(request, category_id):
      posts = Blogs.objects.filter(category__id=category_id)
      context = {
            'posts': posts,
      }
      return render(request, 'posts_by_category.html',context)  

def post_detail(request, slug):
    blog = Blogs.objects.get(slug=slug)
    context = {
        'blog': blog,
    }
    return render(request, 'post_detail.html', context)

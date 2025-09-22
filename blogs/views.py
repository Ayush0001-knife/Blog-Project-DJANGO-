from django.shortcuts import render
from .models import Categorie, Blogs

# Create your views here.
def posts_by_category(request, category_id):
      posts = Blogs.objects.filter(category__id=category_id)
      context = {
            'posts': posts,
      }
      return render(request, 'posts_by_category.html',context)  
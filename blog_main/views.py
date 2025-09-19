from django.shortcuts import render
from blogs.models import Categorie, Blogs
import random

def home(request):
    categories = Categorie.objects.all()
    all_blogs = list(Blogs.objects.all())  # convert queryset to list
    featured_blogs = random.sample(all_blogs, min(len(all_blogs), 3))  # pick 3 random blogs
    
    context = {
        'categories': categories,
        'featured_blogs': featured_blogs,
    }
    return render(request, 'home.html', context)

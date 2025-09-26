from django.urls import path, include
from . import views

urlpatterns = [
      path('<int:category_id>',views.posts_by_category,name='posts_by_category'),
      path('<int:blog_id>', views.post_detail, name='post_detail'),
]
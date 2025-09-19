from django.contrib import admin
from .models import Categorie
from .models import Blogs

# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
      list_display = ('id','Category_name','created_at','updated_at')

class BlogsAdmin(admin.ModelAdmin):
      list_display = ('id','title','category','author','created_at','updated_at')
      prepopulated_fields = {'slug':('title',)}

admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Blogs,BlogsAdmin)

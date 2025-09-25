from .models import Categorie

def get_categories(request):
    categories = Categorie.objects.all()
    return {'categories': categories}
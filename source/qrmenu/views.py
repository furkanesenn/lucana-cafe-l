from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, View

from .models import Category, Meal

# Index view 

class IndexView(View):
    template_name = 'qrmenu/index.html'
    
    def get(self, request):
        return render(request, self.template_name, {'categories': Category.objects.all()}, status=200)

# Category view

class CategoryView(DetailView):
    template_name = 'qrmenu/category.html'

    def get(self, request, category):
        if not Category.objects.filter(name=category).exists():
            raise Http404("Böyle bir kategori yok.")
        
        category = Category.objects.get(name=category)
        meals = category.meals.all()
        return render(request, self.template_name, {'category': category, 'meals': meals}, status=200)
    
# Search view

class SearchView(View):
    template_name = 'qrmenu/search.html'

    def get(self, request):
        query = request.GET.get('query', '')  # Get the 'query' parameter from the POST request
        meals = Meal.objects.filter(name__icontains=query) if query else []
        return render(request, self.template_name, {'meals': meals, 'query': query}, status=200)
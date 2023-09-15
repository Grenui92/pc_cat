from django.shortcuts import render

# Create your views here.
from .models import Categories, Tovar
from django.db.models import Q 
from operator import and_   
import random
from functools import reduce

def create_cats(request):
    for i in range(20):
        Categories.objects.create(name=i)
        
    return render(request, 'first/index.html', context={'text': 'Nice'})

def create_tovar(request):
    cats = Categories.objects.all()
    for i in range(20):
        new_cats = cats
        tov = Tovar.objects.create(name=i)
        for j in range(3):
            cat = random.choice(new_cats)
            tov.categories.add(cat)
            tov.save()
    return render(request, 'first/index.html')       

def all_cats(request):
    return render(request, 'first/index.html', context={'text': Categories.objects.all()})

def show_tovar(request):
    cats_id = [2, 12, 14]
    tovar = Tovar.objects.all()
    for cat in cats_id:
        tovar = tovar.filter(categories=cat)

    print(tovar)
    return render(request, 'first/index.html', context={'text': tovar})
    
    
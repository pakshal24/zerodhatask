from updater.models import bhav
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here
CACHE_TTL = getattr(settings ,'CACHE_TTL' , 60*60*24)

def query(name = None):
    if name:
        print("DATA COMING FROM DB")
        recipes = bhav.objects.filter(name__contains = name)
    else:
        recipes = bhav.objects.all()
    return recipes
def search(response):
    name = response.POST.get("name")
    if(name == None) :
        name = "FULLRESULT"
    if name:
        name = name.upper()
    if cache.get(name) : 
        print("From CACHE")
        print("####################")   
        result = cache.get(name)
    else :
        print("FROM DB")
        print("####################")
        if name=='FULLRESULT':
            result = query(None)
        else:
            result = query(name)
        cache.set(name,result)

    context = {'result' : result , 'equity' : name}
    return render(response,"frontpage/home.html",context)



from django.http.request import HttpRequest
from django.shortcuts import render 
from .models import *
from os import name
# Create your views here.
def nav_cat():
    cat = Categories.objects.all
    return cat

def home(request):
    
    all_posts = Post.objects.all()
    posts_show ={}
    if all_posts.filter(active=True):
        posts_show = all_posts.exclude(active=False)
    show_in_top ={}
    if all_posts.filter(active=True):
        show_in_top = all_posts.exclude(show_in_home=False)
    if all_posts.filter(active=True):
        show_in_first_top = all_posts.exclude(show_in_home_first=False)
    for p in posts_show:
        if (p.id%4) == 0 : 
            p.ads_num = 0
       
    # ads_v = Ads.objects.get(page = 'home' , posision = 'V')
    # ads_h = Ads.objects.get(page = 'home' , posision = 'H')

    data = {
        'post' : posts_show ,
        'post_head' : show_in_top,
        'post_first_head' :show_in_first_top,
        'cat':nav_cat(),
        # 'ads_v':ads_v,
        # 'ads_h':ads_h
    }
    return render(request , 'blog/home.html', data)



def category(request, name):
    cat = Categories.objects.get(cat_name=name)
    all_posts = Post.objects.filter(category = cat.id)
    posts_show ={}
    if all_posts.filter(active=True):
        posts_show = all_posts.exclude(active=False)
    
    data = {
        'post' : posts_show ,
        'c':cat,
        'cat':nav_cat(),
    }
    return render(request , 'blog/categories.html', data)


def single_post(request , post_name):
    post = Post.objects.get(title = post_name)
    data = {
        'post' : post,
    }
   
    return render(request , 'blog/single-post.html', data )

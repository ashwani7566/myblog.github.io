from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category
# Create your views here.
def home(request):
    #load all the post from db
    posts=Post.objects.all()[:12]
    #print(posts)
    cats=Category.objects.all()
    data={
        'posts':posts,
        'cats':cats
    }

    return render(request, 'home.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all()
    #print(post)
    return render(request, 'posts.html',{'post':post,'cats':cats})

def category(request,url):
    cat=Category.objects.get(url=url)
    cats=Category.objects.all()
    posts=Post.objects.filter(cat=cat)
    return render(request, "category.html",{'cat':cat,'cats':cats,'posts':posts})

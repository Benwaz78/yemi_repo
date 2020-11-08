from django.shortcuts import render
from frontend.models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    post = Post.objects.order_by('-created')[:3]
    about = AboutModel.objects.all()[:3]
    context = {
        'pt':post,
        'ab':about
    }
    return render(request, 'frontend/index.html', context)

def about(request):
    about = AboutModel.objects.all()
    return render(request, 'frontend/about.html', {'abt':about})

def about_detail(request, abt_id):
    detail = AboutModel.objects.get(id=abt_id)
    return render(request, 'frontend/detail.html', {'det':detail})

def users(request):
    return render(request, 'frontend/users.html')

def blog(request):
    post = Post.objects.all()
    return render(request, 'frontend/post-list.html', {'pst':post})

# The code below displayspost from a category
def post_from_category(request, cat_id):
    count_post_cat = Post.objects.filter(category__id=cat_id).count()
    category = Category.objects.get(id=cat_id)
    post_cat = Post.objects.filter(category__id=cat_id)
    context = {
                'pst': post_cat, 
                'ct': count_post_cat,
                'category':category
                }

    return render(request, 'frontend/post-cat.html', context)

def single_blog(request, post_id):
    try:
        single = Post.objects.get(id=post_id)
    except:
        return render(request, 'frontend/404.html')
    return render(request, 'frontend/single-blog.html', {'sin':single})

def services(request):
    return render(request, 'frontend/services.html')

def contact(request):
    return render(request, 'frontend/contact.html')

from django.shortcuts import render
from frontend.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# SEND MAIL IMPORTS STARTS HERE
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# SEND MAIL IMPORTS ENDS HERE

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
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phoneNo')
        email = request.POST.get('email')
        referer = request.POST.get('referer')
        gender = request.POST.get('gender')
        message = request.POST.get('message')
        subject = 'Contact Us Form'
        context = {
            'name':name,
            'phone':phone,
            'email':email,
            'referer':referer,
            'gender':gender,
            'message': message,
        }
        html_message = render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <lappyng@gmail.com>'
        email_send = mail.send_mail(subject, plain_message, from_email, [
                    'uwazie.benedict@alabiansolutions.com', 'adeloyeadeyemi@gmail.com'], 
                    html_message=html_message, fail_silently=True)
        if email_send:
            messages.success(request, 'Email is sent')
        else:
            messages.error(request, 'Email is not sent')
 
    return render(request, 'frontend/contact.html')

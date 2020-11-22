from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages


from backend.forms import *
# Create your views here.


@login_required(login_url='/admin-pages/')
def dashboard(request):
    return render(request, 'backend/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')


@login_required(login_url='/admin-pages/')
def confirm_logout(request):
    return render(request, 'backend/confirm-logout.html')


@login_required(login_url='/admin-pages/')
def logout_view(request):
    logout(request)
    return redirect('backend:login_view')


@login_required(login_url='/admin-pages/')
def categroy_form(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            messages.success(request, 'Category Created')
    else:
        cat_form = CategoryForm()
    return render(request, 'backend/add-category.html', {'cat': cat_form})


@login_required(login_url='/admin-pages/')
def post_form(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Post Created')
    else:
        post_form = PostForm()
    return render(request, 'backend/add-post.html', {'post': post_form})


def register(request):
    if request.method == 'POST':
        register = Register(request.POST)
        if register.is_valid():
            register.save()
            messages.success(request, 'User have been registered')
    else:
        register = Register()
    return render(request, 'frontend/register.html', {'reg': register})



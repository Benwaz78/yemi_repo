from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import update_session_auth_hash

from django.contrib import messages

from django.views.generic import(
    ListView, CreateView, 
    DeleteView, DetailView,
    UpdateView
    )

from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

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


@login_required(login_url='/admin-pages/')
def view_categories(request):
    categories = Category.objects.all()
    return render(request, 'backend/view-category.html', {'cat': categories})


@login_required(login_url='/admin-pages/')
def delete_category(request, cat_id):
    delete_cate = Category.objects.get(id=cat_id)
    delete_cate.delete()
    return redirect('backend:view_categories')


@login_required(login_url='/admin-pages/')
def edit_category(request, cat_id):
    single_cat = get_object_or_404(Category, id=cat_id)
    if request.method == 'POST':
        cat_obj = CategoryForm(request.POST, instance=single_cat)
        if cat_obj.is_valid():
            cat_obj.save()
            messages.success(request, 'Category Edited successfully')
    else:
        cat_obj = CategoryForm(instance=single_cat)
    return render(request, 'backend/edit-category.html', {'cat_form':cat_obj})


@login_required(login_url='/admin-pages/')
def single_category(request, cat_id):
    single = get_object_or_404(Category, id=cat_id)
    return render(request, 'backend/single-category.html', {'sin':single})


@login_required(login_url='/admin-pages/')
def pass_form(request):
    if request.method == 'POST':
        pass_form = ChangePassword(data=request.POST, user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user) 
            messages.success(request, 'Password changed successfully.')
    else:
        pass_form = ChangePassword(user=request.user)
    return render(request, 'backend/change-password.html', {'pass_key': pass_form})


@login_required(login_url='/admin-pages/')
def edit_profile_form(request):
    if request.method == 'POST':
        edit_form = EditProfileForm(data=request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditProfileForm(instance=request.user)
    return render(request, 'backend/edit-profile.html', {'edit': edit_form})


class ListCategories(LoginRequiredMixin, ListView):
    login_url = '/admin-pages/'
    model = Category
    template_name = 'backend/class-category.html'
    context_object_name = 'list_cat'


class AddCategory(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/admin-pages/'
    model = Category
    template_name = 'backend/class-add-category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('backend:add_category')
    success_message = 'Category added successfully'


class UpdateCategory(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/admin-pages/'
    model = Category
    template_name = 'backend/class-add-category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('backend:update_category')
    success_message = 'Category updated successfully'








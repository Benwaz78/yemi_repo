from django import forms
from frontend.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm



class Register(UserCreationForm):
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email*',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(label='Enter Password*', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password*', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class meta():
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user



class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(label="Category Name*",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter Category'}))
    desc = forms.CharField(label='Description', required=False,
                               widget=forms.Textarea(
                                   attrs={'class': 'form-control'}
                               ))
    catch_bot = forms.CharField(required=False,
                                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # clean_<fieldname> is use to validate for just one field
    def clean_cat_name(self):
        cat = self.cleaned_data.get('cat_name').lower()
        if Category.objects.filter(cat_name=cat).exists():
            raise forms.ValidationError(f'{cat} already exist')
        return cat

    class Meta():
        fields = '__all__'
        model = Category


class PostForm(forms.ModelForm):
    PUBLISH = 'PB'
    UNPUBLISH = 'UPB'
    FEATURED_VALUES = [
        (PUBLISH, 'Publish'),
        (UNPUBLISH, 'Unpublish')
    ]
    pst_title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Post Title'})
    )
    featured = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'}, choices=FEATURED_VALUES)
        
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    pst_img = forms.ImageField()
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    catch_bot = forms.CharField(required=False,
                                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        exclude = ['created', 'user']
        model = Post

class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(label='Your Old Password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Old Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
                                 validators.MaxLengthValidator(0)])


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(label='Firstname', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(label='Lastname', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email', 'disabled':'disabled'}))
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

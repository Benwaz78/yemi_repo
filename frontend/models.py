from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    desc = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural='Post Category'

class Post(models.Model):
    PUBLISH = 'PB'
    UNPUBLISH = 'UPB'
    FEATURED_VALUES = [
        (PUBLISH, 'Publish'),
        (UNPUBLISH, 'Unpublish')
    ]
    pst_title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    pst_img = models.ImageField(blank=True, null=True, upload_to='uploads/')
    featured = models.CharField(max_length=5, choices=FEATURED_VALUES, default=PUBLISH)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural = 'Post'

class AboutModel(models.Model):
    abt_title = models.CharField(max_length=100)
    abt_image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    biography = models.TextField()

    def __str__(self):
        return self.abt_title

    class Meta():
        verbose_name_plural = 'About Us'


class ContactModel(models.Model):
    CHOOSE = 'Choose'
    FACEBOOK = 'FB'
    TWITTER = 'TW'
    NAIRALAND = 'NL'
    LINKEDIN = 'LN'
    REFERER_FIELD = [
        (CHOOSE, 'Please Choose'),
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (NAIRALAND, 'Nairaland'),
        (LINKEDIN, 'Linkedin')
    ]

    MALE = 'ML'
    FEMALE = 'FM'
    GENDER_FIELD = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=150)
    email = models.EmailField()
    referer = models.CharField(max_length=10, default=CHOOSE, blank=True)
    gender = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

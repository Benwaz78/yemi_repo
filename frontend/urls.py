from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('detail-page/<int:abt_id>/', views.about_detail, name='about_detail'),
    path('blog-pages/', views.blog, name='blog'),
    path('users-page/', views.users, name='users'),
    path('single-blog/<int:post_id>/', views.single_blog, name='single_blog'),
    path('post-cat/<int:cat_id>/',
         views.post_from_category, name='post_from_category'),
    path('service-page/', views.services, name='services'),
    path('contact-page/', views.contact, name='contact'),
]

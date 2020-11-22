from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('logout-view/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-category/', views.categroy_form, name='categroy_form'),
    path('add-post/', views.post_form, name='post_form'),
    path('register-page/', views.register, name='register'),
]

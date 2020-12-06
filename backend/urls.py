from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('logout-view/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pass-form/', views.pass_form, name='pass_form'),
    path('edit-profile-form/', views.edit_profile_form, name='edit_profile_form'),
    path('add-category/', views.categroy_form, name='categroy_form'),
    path('add-post/', views.post_form, name='post_form'),
    path('register-page/', views.register, name='register'),
    path('category-page/', views.view_categories, name='view_categories'),
    path('delete-category/<int:cat_id>/',
         views.delete_category, name='delete_category'),
    path('edit-category/<int:cat_id>/',
         views.edit_category, name='edit_category'),
    path('single-category/<int:cat_id>/',
         views.single_category, name='single_category'),
    path('list-category/',
         views.ListCategories.as_view(), name='list_categories'),
    path('add-category/',
         views.AddCategory.as_view(), name='add_category'),
    path('update-category/<int:pk>/',
         views.UpdateCategory.as_view(), name='up_category'),
]

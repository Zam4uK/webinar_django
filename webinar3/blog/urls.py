from django.urls import path
from .views import blog_list, blog_detail, blog_edit

urlpatterns = [
    path('', blog_list, name="blog_list"),
    path('<int:slug>/', blog_detail, name="blog-detail"),
    path('<int:slug>/edit/', blog_edit, name="blog-edit"),
    path('create/', blog_edit, name="blog-create"),
]

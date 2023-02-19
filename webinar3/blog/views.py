from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    blog_list = Blog.objects.filter(is_active=True)
    return render(request, 'blog/blog_list.html', {'blog_list':blog_list})



def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/blog-detail.html', {'blog':blog})


def blog_edit(request, pk=None):
    blog = None
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(blog_detail)
        return render(request, 'blog/blog_edit.html', {"form":form}) 
    if pk :
        blog = Blog.objects.get(pk=pk)
        form = BlogForm(instance=blog)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_edit.html', {"form":form, "blog":blog})
from django.views import generic
from django.contrib.auth import get_user_model
from django.http import HttpResponse,HttpResponseRedirect

from .models import Blog
from .forms import BlogPost

USER= get_user_model()

class BlogList(generic.ListView):
    queryset = Blog.objects.all()
    template_name = 'blog/blogs.html'
    context_object_name = 'data'

class BlogDetail(generic.DetailView):
    model = Blog
    queryset = Blog.objects.all()
    pk_url_kwarg = 'id'
    template_name = 'blog/readblog.html'
    context_object_name = 'user_obj'

class Create(generic.CreateView):
    form_class = BlogPost
    template_name = 'blog/create.html'
    success_url = '/users/blogs/'


class Delete(generic.DeleteView):
    model = Blog
    success_url = '/users/blogs/'

class Update(generic.UpdateView):
    form_class = BlogPost
    success_url = '/users/blogs'
    model = Blog
    template_name = 'blog/update.html'
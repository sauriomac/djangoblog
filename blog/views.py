# from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostcreateForm
from .models import Post, PostView, Like, Comment

# from django.urls import reverse_lazy

# Create your views here.


# class ListView(View):
#     model = Post



class BlogListView(ListView):
    model = Post

class BlogCreateView(CreateView):
    form_class = PostcreateForm
    model = Post

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context.update({
            'view_type' : 'create',
             'form': PostcreateForm()
        })

        return context

class BlogDetailView(DetailView):
    model = Post

class BlogUpdateView(UpdateView):
    form_class = PostcreateForm
    model = Post
    success_url = "/"

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context.update({
            'view_type' : 'update',
            'form': PostcreateForm()
        })

        return context

class BlogDeleteView(DeleteView):
    model = Post
    success_url = "/"
   
from django.shortcuts import render

# breakdown
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.http import require_POST
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required







class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/blog_home.html'  # Specify your template here
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    paginate_by = 8  # Add pagination (8 posts per page)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'summary', 'content', 'image']  # Add 'image' field

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'summary', 'content', 'image']  # Add 'image' field

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

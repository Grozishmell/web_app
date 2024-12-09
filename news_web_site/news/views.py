from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class NewsAllView(ListView):
    model = Articles
    template_name = 'news/news_home.html'
    context_object_name = 'article'


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsCreateView(CreateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

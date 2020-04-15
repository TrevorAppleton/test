from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import author
from books.models import listofbooks #added this might need to delete it. 
from django.urls import reverse

class AuthorInfoView(DetailView):
    model = author
    pk_url_kwarg = "author_pk"

class AuthorListView(ListView):
    model = author
    pk_url_kwarg = "author_pk"

    #changes what is iterated through in the template from object_list to listofbooks
    context_object_name = 'listofauthors'

#This filters the authors which are related to the listofbooks
    def get_queryset(self, *args, **kwargs):
        return author.objects.filter(booklist=self.kwargs['listofbooks_pk'])

class AuthorCreateView(CreateView):
    model = author
    pk_url_kwarg = "listofbooks_pk"
    fields = ['authorname','authorage']

    def get_success_url(self, *args, **kwargs):
       return reverse('author:author-detail',kwargs={'author_pk':self.object.pk})



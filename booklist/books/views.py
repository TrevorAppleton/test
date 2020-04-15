from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import listofbooks

class BookListView(ListView):
    model = listofbooks
    pk_url_kwarg = "listofbooks_pk"

    #changes what is iterated through in the template from object_list to listofbooks
    context_object_name = 'listofbooks'

class BookDetailView(DetailView):
    model = listofbooks
    pk_url_kwarg = "listofbooks_pk"


class BookCreateView(CreateView):
    model = listofbooks
    pk_url_kwarg = "listofbooks_pk"
    fields = ['booktitle','description']
    success_url = '/' #Home page







    
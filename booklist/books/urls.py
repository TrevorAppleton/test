from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='book-list-view'),
    path('new/', BookCreateView.as_view(), name='book-create'),    
    path('<int:listofbooks_pk>/', BookDetailView.as_view(), name='book-detail'),

]
    
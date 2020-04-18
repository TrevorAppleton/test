from django.urls import path
from .views import AuthorInfoView, AuthorListView, AuthorCreateView

app_name = 'author'
urlpatterns = [
    path('<int:listofbooks_pk>/authors', AuthorListView.as_view(), name='author-list'),
    path('<int:author_pk>', AuthorInfoView.as_view(), name='author-detail'),
    path('<int:listofbooks_pk>/new/', AuthorCreateView.as_view(), name='author-create'),
]
    
    
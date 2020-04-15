from django.contrib import admin
from .models import listofbooks
from author.models import author

admin.site.register(listofbooks)
admin.site.register(author)

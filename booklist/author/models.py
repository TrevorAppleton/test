from django.db import models

class author(models.Model):
    booklist = models.ForeignKey("books.listofbooks",on_delete=models.CASCADE, blank=True, null=True)
    authorname= models.CharField(max_length = 100, null=True)
    authorage = models.IntegerField()
    
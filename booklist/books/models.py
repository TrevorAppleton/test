from django.db import models

class listofbooks(models.Model):
    booktitle = models.CharField(max_length = 100)
    description = models.TextField(null=True) 


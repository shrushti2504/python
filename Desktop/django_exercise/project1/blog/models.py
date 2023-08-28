from django.db import models

# Create your models here.

class Author(models.Model):
    author_name=models.CharField(max_length=20)
    information=models.TextField()

class Blogs(models.Model):
    title=models.CharField(max_length=20)
    post_date=models.DateField()
    author_name=models.ForeignKey(Author,on_delete=models.CASCADE)
    content=models.TextField()

class Comment(models.Model):
    comments=models.TextField()


from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Comment on Post {self.post.id}'
from django.db import models

# Create your models here.

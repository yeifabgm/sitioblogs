from django.db import models
from posts.models import Post

class Tag(models.Model):
    post = models.ForeignKey(Post, db_column='post')
    palabra = models.CharField(max_length=45, blank=False, unique=True)
    def __str__(self):
        return self.palabra
    class Meta:
        db_table = 'blogs_tag'
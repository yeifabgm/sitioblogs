from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comentario(models.Model):
    post = models.ForeignKey(Post, db_column='post')
    user = models.ForeignKey(User, null=True, db_column='user', blank=True)
    email = models.EmailField(max_length=70, blank=True, null= True)
    comentario = models.TextField(max_length=1000, blank=False)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comentario
    class Meta:
        db_table = 'blogs_comentario'
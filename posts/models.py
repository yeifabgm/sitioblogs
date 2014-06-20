from django.db import models
from ckeditor.fields import RichTextField
from blogs.models import Adminblog

class Post(models.Model):
    adminblog = models.ForeignKey(Adminblog, db_column='adminblog')
    titulo = models.CharField(max_length=100, blank=False)    
    descripcion = models.TextField(max_length=1000, blank=False)
    contenido = RichTextField()
    fecha_crea = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
    class Meta:
        db_table = 'blogs_post'
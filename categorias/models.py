from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(max_length=300, blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'blogs_categoria'
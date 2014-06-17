# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from categorias.models import Categoria
from django.contrib.auth.models import User

class Blog(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(max_length=1000, blank=False)
    categoria = models.ForeignKey(Categoria, db_column='categoria')
    fecha_crea = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'blogs_blog'

class Permiso(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    descripcion = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'blogs_permiso'

class Adminblog(models.Model):
    blog = models.ForeignKey('Blog', db_column='blog')
    user = models.ForeignKey(User, db_column='user')
    permiso = models.ForeignKey('Permiso', db_column='permiso')
    def __str__(self):
        return u"%s es %s de %s" % (self.user, self.permiso, self.blog)
    class Meta:
        db_table = 'blogs_adminblog'




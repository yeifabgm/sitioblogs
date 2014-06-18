# -*- coding: utf-8 -*-

from blogs.models import Adminblog, Blog, Permiso
from blogs.form import BlogForm
from posts.models import Post
from categorias.models import Categoria

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import TemplateView, ListView

def index(request):
	return HttpResponse("¡¡Estamos creando nuestra primera view!!")

@login_required
def blogCrear(request):
	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			blogCrea = Blog.objects.create(
				nombre=form.cleaned_data['nombre'],
				descripcion=form.cleaned_data['descripcion'],
				categoria=form.cleaned_data['categoria'],
				fecha_crea=timezone.now()
				)
			adminiblog = Adminblog.objects.create(
				blog=blogCrea,
				user=request.user,
				permiso=Permiso.objects.get(pk=1)
				)
			adminiblog.save()
	else:
		form = BlogForm()
	return render_to_response('blogs/blog_crear.html', {'form': form}, context_instance=RequestContext(request))

def blog(request, id_blog):
	blogs = Blog.objects.filter(pk=id_blog)
	posts = Post.objects.filter(adminblog__blog__id=id_blog)
	return render_to_response('blogs/blogs.html', {'posts': posts, 'blogs': blogs}, context_instance=RequestContext(request))

@login_required
def blogsUsuario(request):
	blogs = Adminblog.objects.filter(user=request.user.id, permiso=1)
	return render_to_response('blogs/blog_usuario.html', {'blogs': blogs}, context_instance=RequestContext(request))

@login_required
def blogsUsuarioFavoritos(request):
	blogs = Adminblog.objects.filter(user=request.user.id, permiso=3)
	return render_to_response('blogs/blog_usuario.html', {'blogs': blogs}, context_instance=RequestContext(request))

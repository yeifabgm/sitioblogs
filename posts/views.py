from posts.models import Post
from blogs.models import Adminblog, Blog
from comentarios.models import Comentario
from posts.form import PostForm
from comentarios.form import ComentarioForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from django.db.models import Count

@login_required
def crearPost(request):
	if  request.POST.get("id_blog", "") != '':
		request.session["id_blog"] = request.POST.get("id_blog", "")
		form = PostForm()
	else:
		if request.method == 'POST':
			form = PostForm(request.POST)
			if form.is_valid():
				
				adminblog = Adminblog.objects.get(blog=request.session["id_blog"], user=request.user, permiso__in=[1,2])
				post = Post.objects.create(
					adminblog=adminblog,
					titulo=form.cleaned_data['titulo'],
					descripcion=form.cleaned_data['descripcion'],
					contenido=form.cleaned_data['contenido'],
					fecha_crea=timezone.now()
					)
				post.save()
		else:
			form = PostForm()
	return render_to_response("posts/post_crear.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def postUsuario(request, id_blog):
	post = Post.objects.filter(adminblog__user=request.user, adminblog__post=id_blog)
	return render_to_response("post_usuario.html", {'form': form}, context_instance=RequestContext(request))

def verPost(request, id_post):
	post = Post.objects.get(pk=id_post)
	postsRecientes = Post.objects.filter(adminblog__blog__id=post.adminblog.blog.id).order_by('-fecha_crea')[0:6]
	comentarios = Comentario.objects.filter(post__id=id_post)

	if request.method == 'POST':
		form = ComentarioForm(request.POST)
		if form.is_valid():
			if request.user.is_authenticated():
				comentario = Comentario.objects.create(
					post = form.cleaned_data['post'],
					user = request.user,
					email = request.user.email,
					comentario=form.cleaned_data['comentario'],
					fecha_crea=timezone.now()
					)
			else:
				comentario = Comentario.objects.create(
					post = form.cleaned_data['post'],
					email = form.cleaned_data['email'],
					comentario = form.cleaned_data['comentario'],
					fecha_crea = timezone.now()
					)
			comentario.save()
	else:
		form = ComentarioForm()
	return render_to_response("posts/post.html", {'post': post, 'postsRecientes': postsRecientes, 'comentarios': comentarios}, context_instance=RequestContext(request))






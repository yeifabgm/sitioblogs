from posts.models import Post
from blogs.models import Adminblog, Blog
from posts.form import PostForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import TemplateView, ListView

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

def postUsuario(request, id_blog):
	post = Post.objects.filter(adminblog__user=request.user, adminblog__post=id_blog)
	return render_to_response("post_usuario.html", {'form': form}, context_instance=RequestContext(request))








from django.conf.urls import patterns, include, url
from django.contrib import admin
from sitioblogs.views import Usuario
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^upload/', 'ckeditor.views.upload', name='ckeditor_upload'),
	url(r'^browse/', 'ckeditor.views.browse', name='ckeditor_browse'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/(?P<usuario>[-\w]+)/$', Usuario.as_view()),

	# Examples:
    # url(r'^$', 'sitioblogs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'sitioblogs.views.login_page', name="login"),
    url(r'^logout/$', 'sitioblogs.views.logout_view', name="logout"),
    url(r'^$', 'sitioblogs.views.homepage', name="homepage"),

    # Blogs
    url(r'^blogs/$', 'blogs.views.index'),
    url(r'^blogs/(?P<id_blog>\d+)/$', 'blogs.views.blog', name="blog_detalle"),
    url(r'^blogs/crear/$', 'blogs.views.blogCrear', name="blog_crear"),
    url(r'^blogs/usuario/$', 'blogs.views.blogsUsuario', name="blog_usuario"),
    url(r'^blogs/favoritos/$', 'blogs.views.blogsUsuarioFavoritos', name="blog_favoritos"),

    # Posts
    url(r'^posts/crear/$', 'posts.views.crearPost', name="post_crear"),
    url(r'^posts/(?P<id_post>\d+)/$', 'posts.views.verPost', name="post_ver"),

    # Comentarios
    
    
)

urlpatterns += staticfiles_urlpatterns()
# -*- coding: utf-8 -*-

from django.contrib import admin
from blogs.models import Blog, Permiso, Adminblog

admin.site.register(Blog)
admin.site.register(Permiso)
admin.site.register(Adminblog)

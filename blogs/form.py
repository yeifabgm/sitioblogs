from django import forms
from blogs.models import Blog

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		

#class BlogForm(forms.Form):
#	nombre = forms.CharField(max_length=100, required=True)
#	descripcion = forms.CharField(widget=forms.Textarea, required=True)

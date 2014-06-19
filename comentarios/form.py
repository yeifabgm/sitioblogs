from django import forms
from comentarios.models import Comentario

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
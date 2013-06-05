from django import forms
from miniapp.apps.ieso.models import horario,materia,grupo,profesor,alumno

class addAlumnoForm(forms.ModelForm):
	class Meta:
		model 	= 	alumno

class addProfesorForm(forms.ModelForm):
	class Meta:
		model	=	profesor

class addMateriaForm(forms.ModelForm):
	class Meta:
		model 	=	materia

class addHorarioForm(forms.ModelForm):
	class Meta:
		model 	=	horario

class addGrupoForm(forms.ModelForm):
	class Meta:
		model 	=	grupo
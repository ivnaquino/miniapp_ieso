from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http	import HttpResponseRedirect
from miniapp.apps.ieso.models import alumno,profesor,materia,horario,grupo
from miniapp.apps.ieso.forms import addAlumnoForm,addProfesorForm,addMateriaForm,addHorarioForm,addGrupoForm

def index_view(request):
	alum 	= alumno.objects.all().order_by('apellidoPat')
	prof 	= profesor.objects.all()
	grup 	= grupo.objects.all().order_by('nombre','cuatrimestre')
	ctx = {'alumnos':alum,'profesores':prof,'grupos':grup}
	return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

def alumnos_view(request):
	alum = alumno.objects.all()
	ctx = {'alumnos':alum}
	return render_to_response('home/alumnos.html',ctx,context_instance=RequestContext(request))

def alumno_view(request,id_alumno):
	alum = alumno.objects.get(id=id_alumno)
	grup = grupo.objects.get(pk=alum.grupo.id)
	mats = grup.materia.all()
	ctx = {'alumno':alum,'grupo':grup,'materias':mats}
	return render_to_response('home/alumno.html',ctx,context_instance=RequestContext(request))

def profesor_view(request,id_profesor):
	prof = profesor.objects.get(id=id_profesor)
	grups = prof.grupo.all()
	ctx = {'profesor':prof,'grupos':grups}
	return render_to_response('home/profesor.html',ctx,context_instance=RequestContext(request))

def grupo_view(request,id_grupo):
	grup 	= grupo.objects.get(id=id_grupo)
	alumns 	= alumno.objects.filter(grupo = id_grupo).order_by('apellidoPat')
	mats 	= grup.materia.all()
	ctx 	= {'grupo':grup, 'alumnos':alumns,'materias':mats}
	return render_to_response('home/grupo.html',ctx,context_instance=RequestContext(request))


##################################################################################################################
##				Vistas para los formularios	de Registro														    ##
##################################################################################################################

def add_alumno_view(request):
	if request.method == 'POST':
		form 	= 	addAlumnoForm(request.POST)
		if form.is_valid():
			add =	form.save(commit=False)
			add.save()
			form.save_m2m()
			return HttpResponseRedirect('/')
	else:
		form 	=	addAlumnoForm()

	ctx 	=	{'titulo':'Agregar Alumno','idForm':'formAlumno','form':form}
	return render_to_response('home/formularios.html',ctx,context_instance=RequestContext(request))

def add_profesor_view(request):
	if request.method == 'POST':
		form 	= 	addProfesorForm(request.POST)
		if form.is_valid():
			add =	form.save(commit=False)
			add.save()
			form.save_m2m()
			return HttpResponseRedirect('/')
	else:
		form 	=	addProfesorForm()

	ctx 	=	{'titulo':'Agregar Profesor','idForm':'formProfesor','form':form}
	return render_to_response('home/formularios.html',ctx,context_instance=RequestContext(request))

def add_horario_view(request):
	if request.method == 'POST':
		form = addHorarioForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			return HttpResponseRedirect('/')
	else:
		form = addHorarioForm()
	ctx  = {'titulo':'Agregar horario','idForm':'formHorario','form':form}
	return render_to_response('home/formularios.html',ctx,context_instance=RequestContext(request))

def add_materia_view(request):
	if request.method == 'POST':
		form = addMateriaForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			return HttpResponseRedirect('/')
	else:
		form = addMateriaForm()
	ctx = {'titulo':'Agregar Materia','idForm':'formMateria','form':form}
	return render_to_response('home/formularios.html',ctx,context_instance=RequestContext(request))

def add_grupo_view(request):
	if request.method == 'POST':
		form = addGrupoForm(request.POST)
		if form.is_valid():
			add = form.save()
			add.save()
			return HttpResponseRedirect('/')
	else:
		form = addGrupoForm()
	ctx = {'titulo':'Agregar Grupo','idForm':'formGrupo','form':form}
	return render_to_response('home/formularios.html',ctx,context_instance=RequestContext(request))

##################################################################################################################
##				Vistas para los formularios	de Edicion de campos											    ##
##################################################################################################################

def edit_alumno_view(request,id_form):
	alum 	= alumno.objects.get(pk=id_form)
	if request.method == 'POST':
		form = addAlumnoForm(request.POST,instance=alum)
		if form.is_valid():
			edit_alum = form.save(commit=False)
			form.save_m2m()
			edit_alum.save()
			return HttpResponseRedirect('/')
	else:
		form = addAlumnoForm(instance=alum)
	ctx = {'titulo':'Editar Alumno','idForm':'formAlumno','form':form}
	return render_to_response('home/formularios.html',ctx,context_instance=RequestContext(request))

def edit_profesor_view(request,id_form):
	prof 	= profesor.objects.get(pk=id_form)
	if request.method == 'POST':
		form = addProfesorForm(request.POST,instance=prof)
		if form.is_valid():
			edit_prof = form.save(commit=False)
			form.save_m2m()
			edit_prof.save()
			return HttpResponseRedirect('/')
	else:
		form = addProfesorForm(instance=prof)
	ctx = {'titulo':'Editar profesor','idForm':'formProfesor','form':form}
	return render_to_response('home/formularios.html',ctx,context_instance=RequestContext(request))

def edit_materia_view(request,id_form):
	mater = materia.objects.get(pk=id_form)
	if request.method == 'POST':
		form = addMateriaForm(request.POST,instance=mater)
		if form.is_valid():
			edit_materia = form.save(commit=False)
			form.save_m2m()
			edit_materia.save()
			return HttpResponseRedirect('/')
	else:
		form = addMateriaForm(instance=mater)
	ctx= {'titulo':'Editar materia','idForm':'formMateria','form':form}
	return render_to_response('home/formularios.html',ctx,context_instance=RequestContext(request))

def edit_grupo_view(request,id_form):
	grup = grupo.objects.get(pk=id_form)
	if request.method == 'POST':
		form = addGrupoForm(request.POST, instance=grup)
		if form.is_valid():
			edit_grupo = form.save(commit=False)
			form.save_m2m()
			edit_grupo.save()
			return HttpResponseRedirect('/')
	else:
		form = addGrupoForm(instance=grup)
	ctx= {'titulo':'Editar grupo','idForm':'formGrupo','form':form}
	return render_to_response('home/formularios.html',ctx,context_instance=RequestContext(request))
##################################################################################################################
##				Vistas la eliminacion de campos de la base de datos											    ##
##################################################################################################################

def delete_alumno_view(request,id_alumno):
	alumn = alumno.objects.get(pk=id_alumno)
	alumn.delete()

	return HttpResponseRedirect('/')

def delete_profesor_view(request,id_profesor):
	prof = profesor.objects.get(pk=id_profesor)
	prof.delete()

	return HttpResponseRedirect('/')

def delete_materia_view(request,id_materia):
	mater = materia.objects.get(pk=id_materia)
	mater.delete()

	return HttpResponseRedirect('/')

def delete_grupo_view(request,id_grupo):
	grup = grupo.objects.get(pk=id_grupo)
	grup.delete()

	return HttpResponseRedirect('/')

def delete_horario_view(request,id_horario):
	hor = horario.objects.get(pk=id_horario)
	hor.delete()

	return HttpResponseRedirect('/')
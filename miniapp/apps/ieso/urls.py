from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('miniapp.apps.ieso.views',
	url(r'^alumno/(?P<id_alumno>.*)$','alumno_view',name='vista_alumno'),	#especificaciones del alumno
	url(r'^profesor/(?P<id_profesor>.*)$','profesor_view',name='vista_profesor'), #especificaciones del profesor
	url(r'^grupo/(?P<id_grupo>.*)$','grupo_view',name='vista_grupo'),		#especificaciones del grupo
	url(r'^$','index_view',name='vista_principal'),
	url(r'^alumnos$','alumnos_view',name='vista_alumnos'),
	url(r'^agregar/alumno$','add_alumno_view',name='vista_agregar_alumno'),			#Add alumno
	url(r'^agregar/profesor$','add_profesor_view',name='vista_agregar_profesor'),	#Add profesor
	url(r'^agregar/materia$','add_materia_view',name='vista_agregar_materia'),		#Add materia
	url(r'^agregar/grupo$','add_grupo_view',name='vista_agregar_grupo'),			#Add grupo
	url(r'^agregar/horario$','add_horario_view',name='vista_agregar_horario'),		#Add horario
	url(r'^editar/alumno/(?P<id_form>.*)$','edit_alumno_view',name='vista_editar_alumno'),			#Editar alumno
	url(r'^editar/profesor/(?P<id_form>.*)$','edit_profesor_view',name='vista_editar_profesor'),	#Editar profesor
	url(r'^editar/grupo/(?P<id_form>.*)$','edit_grupo_view',name='vista_editar_grupo'),	#Editar grupo
	url(r'^editar/materia/(?P<id_form>.*)$','edit_materia_view',name='vista_editar_materia'),	#Editar materia
	url(r'^eliminar/alumno/(?P<id_alumno>.*)$','delete_alumno_view',name='vista_eliminar_alumno'),	#Eliminar alumno
	url(r'^eliminar/profesor/(?P<id_profesor>.*)$','delete_profesor_view',name='vista_eliminar_profesor'),	#Eliminar profesor
	url(r'^eliminar/grupo/(?P<id_grupo>.*)$','delete_grupo_view',name='vista_eliminar_grupo'),	#Eliminar grupo
	url(r'^eliminar/materia/(?P<id_materia>.*)$','delete_materia_view',name='vista_eliminar_materia'),	#Eliminar materia
	url(r'^eliminar/horario/(?P<id_horario>.*)$','delete_horario_view',name='vista_eliminar_horario'),	#Eliminar horario
)

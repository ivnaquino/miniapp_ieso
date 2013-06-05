from django.db import models

class horario(models.Model):
	TURNOS = (
		('M','Matutino'),
		('V','Vespertino')
		)
	DIAS =(
		('L','Lunes'),
		('Ma','Martes'),
		('Mi','Miercoles'),
		('J','Jueves'),
		('V','Viernes'),
		)
	inicio		= models.TimeField(help_text='Formato hh:mm:ss')
	fin			= models.TimeField(help_text='Formato hh:mm:ss')
	turno 		= models.CharField(max_length=50, choices=TURNOS)
	dia 		= models.CharField(max_length=20, choices=DIAS)

	def __unicode__(self):
		if(self.dia == 'L'):
			dia_s = 'Lunes'
		if(self.dia == 'Ma'):
			dia_s = 'Martes'
		if(self.dia == 'Mi'):
			dia_s = 'Miercoles'
		if(self.dia == 'J'):
			dia_s = 'Jueves'
		if(self.dia == 'V'):
			dia_s = 'Viernes'
		return '%s %s-%s'%(dia_s,self.inicio,self.fin)


class materia(models.Model):
	nombre 		= models.CharField(max_length=50)
	horario 	= models.ForeignKey(horario, related_name='+ref',blank=True)

	def __unicode__(self):
		return self.nombre

class grupo(models.Model):
	nombre 		 = models.CharField(max_length=50,help_text='Nombre del grupo')
	cuatrimestre = models.IntegerField()
	materia		= models.ManyToManyField(materia, blank=True)

	def __unicode__(self):
		return '%s %d'%(self.nombre,self.cuatrimestre)

class profesor(models.Model):
	matricula 	= models.CharField(max_length=100, unique=True, help_text='Matricula')
	nombre 		= models.CharField(max_length=100, help_text='Nombre')
	apellidoPat = models.CharField(max_length=100, help_text='Apellido Paterno', verbose_name='Apellido Paterno')
	apellidoMat = models.CharField(max_length=100, help_text='Apellidio Materno', verbose_name='Apellidio Materno')
	direccion	= models.CharField(max_length=200, blank=True, help_text='Introduzca su direccion')
	telefono	= models.CharField(max_length=50, help_text='Introduzca su numero telefonico 951-000-000',blank=True)
	grupo		= models.ManyToManyField(grupo, blank=True)

	def __unicode__(self):
		return "%s %s %s"%(self.nombre, self.apellidoPat, self.apellidoMat)

class alumno(models.Model):
	matricula 	= models.CharField(max_length=100, unique=True, help_text='Matricula')
	nombre 		= models.CharField(max_length=100, help_text='Nombre')
	apellidoPat = models.CharField(max_length=100, help_text='Apellido Paterno', verbose_name='Apellido Paterno')
	apellidoMat = models.CharField(max_length=100, help_text='Apellidio Materno', verbose_name='Apellido Materno')
	direccion	= models.CharField(max_length=200, blank=True, help_text='Introduzca su direccion')
	telefono	= models.CharField(max_length=50, help_text='Introduzca su numero telefonico 951-000-000',blank=True)
	grupo 		= models.ForeignKey(grupo, blank=True)

	def __unicode__(self):
		return "%s %s %s"%(self.nombre, self.apellidoPat, self.apellidoMat)



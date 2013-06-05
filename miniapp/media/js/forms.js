$(document).on('ready',function(){
	var formulario = $('form').attr('id');
	
	if(formulario == 'formAlumno')
	{
		$('form span').remove();
		$('form label').attr('class','span2');
		$('form input').attr('class','span4');
		$('form select').attr('class','span4');
		$('form #enviar').attr('class','span6 btn btn-primary');	
		

		$('form #id_matricula').attr('placeholder','Matricula');
		$('form #id_nombre').attr('placeholder','Nombre');
		$('form #id_apellidoPat').attr('placeholder','Apellido Paterno');
		$('form #id_apellidoMat').attr('placeholder','Apellido Materno');
		$('form #id_direccion').attr('placeholder','Direccion');
		$('form #id_telefono').attr('placeholder','Telefono');
	}
	if(formulario == 'formProfesor')
	{
		$('span').remove();
		$('label').attr('class','span2');
		$('input').attr('class','span4');
		$('select').attr({
			'class':'span4',
			'size':'10'
		});
		$('#enviar').attr('class','span6 btn btn-primary');


		$('form #id_matricula').attr('placeholder','Matricula');
		$('form #id_nombre').attr('placeholder','Nombre');
		$('form #id_apellidoPat').attr('placeholder','Apellido Paterno');
		$('form #id_apellidoMat').attr('placeholder','Apellido Materno');
		$('form #id_direccion').attr('placeholder','Direccion');
		$('form #id_telefono').attr('placeholder','Telefono');
	}
	if(formulario == 'formMateria')
	{
		$('span').remove();
		$('label').attr('class','span2');
		$('input').attr('class','span4');
		$('select').attr({
			'class':'span4'
		});
		$('#enviar').attr('class','span6 btn btn-primary');
	}
	if(formulario == 'formGrupo')
	{
		$('span').remove();
		$('label').attr('class','span2');
		$('input').attr('class','span4');
		$('select').attr({
			'class':'span4',
			'size':'10'
		});
		$('#enviar').attr('class','span6 btn btn-primary');
	}
	if(formulario == 'formHorario')
	{
		$('span').remove();
		$('label').attr('class','span2');
		$('input').attr('class','span4');
		$('select').attr({
			'class':'span4'
		});
		$('#enviar').attr('class','span6 btn btn-primary');

		$('form #id_inicio').attr('placeholder','HH:MM:SS');
		$('form #id_fin').attr('placeholder','HH:MM:SS');
	}
	
});
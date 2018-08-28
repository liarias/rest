(function(){
	$("#botonEnviarServicio").click(agregar);
	servicios();	
})();

function agregar(){
	console.log("entra boton enviar");
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    info ={}
    info.owner=Number($(".userId").attr("id")),
    info.nombre=$("#selectServicio").val(),
    info.ciudad="Guayaquil";
    info.direccion=$("#direccion").val();
    info.fecha=$("#fecha").val();
    info.pago=0;
    console.log(info)
    $.ajax({
        url: "/servicio/crearServicio/",
        type:"POST",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :function(respuesta) {
        	console.log("exito enviar");
            alert("servicio cargada con éxito");
        },
        error : function(xhr, status) {
        	console.log("error");
            alert(xhr['responseJSON']);
        },
    });
	
}
function servicios(){
	console.log("entra servicios");
    $.ajax({
        url: "/servicio/crearServicio/",
        type:"GET",    
        dataType : 'json',
        success: cargarServicios,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los Servicios.');
        }
    });
}
function cargarServicios(data){
	console.log("entra cargar");
	var serviciosUnicos=[];

    for (servicio of data) {
    	if(!serviciosUnicos.includes(servicio.nombre)){
    		serviciosUnicos.push(servicio.nombre)
    		opcionServicio= '<option value='+servicio.nombre+'>' + servicio.nombre + '</option>';
    		$('#selectServicio').append(opcionServicio);
    	}
    	
    }
    
}
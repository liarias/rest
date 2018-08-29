(function(){
	$("#botonEnviarServicio").click(agregar);
	servicios();	
})();

function agregar(){
	console.log("entra boton enviar");
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    info ={}
    info.persona=Number($(".userId").attr("id")),
    info.servicio=Number($("#selectServicio").val());
    info.fecha=$("#fecha").val();
    info.ciudad="Guayaquil";
    info.direccion=$("#direccion").val();
    
    console.log(info)
    $.ajax({
        url: "/api/guardarServicio/",
        type:"POST",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :function(respuesta) {
        	console.log("exito enviar");
            alert("servicio cargada con éxito");
            window.location = "/persona/"+$(".userId").attr("id");
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
        url: "/api/cargarServicios/",
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

    for (servicio of data) {
    	
		opcionServicio= '<option value='+servicio.id+'>' + servicio.nombre + '</option>';
		$('#selectServicio').append(opcionServicio);
    	
    	
    }
    
}
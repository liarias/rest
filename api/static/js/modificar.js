(function(){
	$("#botonModificarServicio").click(modificar);
    $("#botonEliminarServicio").click(eliminar);
})();

function modificar(){
	console.log("entra boton modificar");
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    info ={}
    info.persona=Number($(".userId").attr("id")),
    info.servicio=Number($(".servicioId").attr("id"));
    info.ciudad="Guayaquil";
    info.direccion=$("#direccion").val();
    
    console.log(info)
    $.ajax({
        url: "/api/modificar/"+$("#botonModificarServicio").attr("val")+"/",
        type:"PUT",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :function(respuesta) {
        	console.log("exito enviar");
            alert("modificado con éxito");
        },
        error : function(xhr, status) {
        	console.log("error");
            alert(xhr['responseJSON']);
        },
    });
	
}
function eliminar(){
    console.log("entra boton eliminar");
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    
    $.ajax({
        url: "/api/eliminar/"+$("#botonEliminarServicio").attr("val"),
        type:"DELETE",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        success :function(respuesta) {
            alert("eliminado con éxito");
            window.location = "/persona/"+$(".userId").attr("id");
        },
        error : function(xhr, status) {
            console.log("error");
            alert(xhr['responseJSON']);
        },
    });
    
}
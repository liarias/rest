function agregarUsuarios(lista){
    html = "";
    for (var i = 0; i < lista.length; i++) {
        html += '<div class="col-md-3 text-center">';
        html += '<a href="/usuariodetalles/' + lista[i].id + '"> <img class="rounded-circle img-circle" src="../../static/img/img.jpg" width="50%" ></a>';
        html += '<h4>' + lista[i].nombre + '</h4>';
        html += '<h5>' + lista[i].ciudad + '</h5>';
        html += '<p class="text-left">Servicios:</p>';
        html += '<ul class="text-left"> ';
        for (var j = 0; j < lista[i].servicios.length; j++) {
            html += '<li>' + lista[i].servicios[j].servicio.nombre + '</li>';
        }   
        html += '</ul> </div>';
    }
    $("div.container div.contenido").append(html);  
};
//
$(document).ready(function() {
    $.ajax({
        url: "/usuarios/",
        type:"GET",   
        dataType : 'json',
        success :agregarUsuarios,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar la lista de usuarios.');
        }
    });
});




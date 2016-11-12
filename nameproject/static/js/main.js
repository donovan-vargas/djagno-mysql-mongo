// using jQuery
$(document).ready(function() {
    $('#cobros tr').click(function() {
        var search = 0;
        $(this).each(function() {
            search = $(this).find(".referencia").html();
            console.log(search)
            buscar(search);
        });
    });

    function buscar(search) {
        $('#detalle tr').show();
        $('#pago tr').show();
        $('#detalle thead tr').show()
        $('#pago thead tr').show()
        if (search.length > 0) {
            $('#detalle tr td.referencia').not(":Contains('" + parseInt(search) + "')").parent().hide('slow');
            $('#pago tr td.referencia').not(":Contains('" + parseInt(search) + "')").parent().hide('slow');
        }
    }
    $(window).scroll(function() {
        if ($(this).scrollTop() > 50) /*height in pixels when the navbar becomes non opaque*/ {
            $('.navbar').addClass('navbar-opac');
        } else {
            $('.navbar').removeClass('navbar-opac');
        }
    });
    $('#dtpick').datepicker({
        format: 'yyyy-mm-dd'
    });
    /*$('#searching').click(function() {
     $.ajax({
     url: '/cobros/search_data/',
     type: 'GET',
     data: {'q': $('#q').val()},
     })
     .success(function(json) {
     $('#q').val('')
     console.log("success");
     console.log(json);
     })
     .fail(function(xhr,errmsg,err) {
     $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
     console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
     })
     .always(function() {
     console.log("complete");
     });

     });*/
});

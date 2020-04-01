$(document).ready(function(){

    // Initialize materialize data picker
    $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
    $('select').formSelect();
    $('.tooltipped').tooltip();

});

// ----- Close message
$('.message-close').click(function() {
    $(this).parent().parent('.card-panel').fadeOut()
});

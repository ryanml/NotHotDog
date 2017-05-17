$(document).ready(function() {

    $('#img-form').submit(function(event) {
        event.preventDefault();

        $.ajax({
            url: '/is-hot-dog',
            type: 'POST',
            processData: false,
            contentType: false,
            dataType: 'json',
            data: new FormData($(this)[0]),

            success: function(responseData) {
                console.log('Success: ', responseData);
            },
            error: function() {
                console.log('Something went wrong.');
            }
        });
    });

});
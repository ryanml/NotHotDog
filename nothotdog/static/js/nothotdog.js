$(document).ready(function() {

    $('form').submit(function(event) {
        event.preventDefault();

        var img = document.getElementById('img');

        if (img.files && img.files[0]) {
            var fileReader = new FileReader();
            fileReader.onload = function(event) {
                $('.img-area').html(
                    `<img src='${event.target.result}'/>`
                );
            }
            fileReader.readAsDataURL(img.files[0]);
        }


        $.ajax({
            url: '/is-hot-dog',
            type: 'POST',
            processData: false,
            contentType: false,
            dataType: 'json',
            data: new FormData($(this)[0]),

            success: function(responseData) {
                if (responseData.is_hot_dog === 'true') {
                    $('.status').text('HOT DOG');
                } else {
                    $('.status').text('NOT HOT DOG');
                }
            },
            error: function() {
                console.log('Something went wrong.');
            }
        });
    });

});
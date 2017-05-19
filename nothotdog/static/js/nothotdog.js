$(document).ready(function() {

    $('#img').change(function(event) {
        var obj = $(this)[0];

        if (obj.files && obj.files[0]) {
            var fileReader = new FileReader();
            fileReader.onload = function(event) {
                $('.img-area').html(
                    `<img class='loaded-img' src='${event.target.result}'/>`
                );
            }
            fileReader.readAsDataURL(obj.files[0]);           
        }
    });

    $('form').submit(function(event) {
        event.preventDefault();

        var $status = $('.status');
        $status.html(
            `<span class='eval'>Evaluating...</span>`
        );

        $.ajax({
            url: '/is-hot-dog',
            type: 'POST',
            processData: false,
            contentType: false,
            dataType: 'json',
            data: new FormData($(this)[0]),

            success: function(responseData) {
                if (responseData.is_hot_dog === 'true') {
                    $status.html(
                        `<span class='result success'>Hot Dog</span>
                         <span class='confidence'>${responseData.confidence}% confident</span>`
                    );
                } else {
                    $status.html(
                        `<span class='result failure'>Not Hot Dog</span>`
                    );
                }
            },
            error: function() {
                console.log('Something went wrong.');
            }
        });
    });

});
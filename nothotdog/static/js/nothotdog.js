$(document).ready(function() {
    var $status = $('.status');

    $('#img').change(function(event) {
        var obj = $(this)[0];

        $status.html('');

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

        if ($('#img')[0].files.length === 0) {
            return false;
        }

        var imageData = new FormData($(this)[0]);

        $status.html(
            `<span class='eval'>Evaluating...</span>`
        );

        $.ajax({
            url: '/is-hot-dog',
            type: 'POST',
            processData: false,
            contentType: false,
            dataType: 'json',
            data: imageData,

            success: function(responseData) {
                if (responseData.is_hot_dog === 'true') {
                    $status.html(
                        `<span class='result success'>Hot Dog</span>
                         <span class='confidence'>${responseData.confidence}% confident</span>`
                    );
                } else {
                    if (responseData.error === 'bad-type') {
                        $status.html(
                            `<span class='eval'>Valid file types are .jpg and .png</span>`
                        );
                    } else {
                        $status.html(
                            `<span class='result failure'>Not Hot Dog</span>`
                        );
                    }
                }
            },
            error: function() {
                $status.html(
                    `<span class='eval'>Something went wrong, try again later.</span>`
                );
            }
        });
    });

});
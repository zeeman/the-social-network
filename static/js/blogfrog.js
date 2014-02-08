$(document).ready(function() {
    $('.message .close').on('click', function() {
        $(this).closest('.message').fadeOut();
    });

    $('.ui.popup').popup({
        on: 'click'
    });
});

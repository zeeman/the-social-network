$(document).ready(function() {
    $('.message .close').on('click', function() {
        $(this).closest('.message').fadeOut();
    });

    $('.ui.popup').popup({
        on: 'click'
    });

    $('form').on('submit', function() {
        event.preventDefault();
        ajax_form_submit(this);
    });
});

function ajax_form_submit(form) {
    var post_data = $(form).find(':input').serializeArray()
    $.post(form.target, post_data, function(data) {
        window.location = $(form).attr('success');
    }, 'json').fail(function(data) {
        set_errors(form, data.responseJSON);
    });
}

function set_errors(form, errors) {
    $(form).find('span.error').remove();
    $(form).find('div.error').removeClass('error');

    $.each(errors, function (name, text) {
        $(form).find('label[for=' + name + ']').first().after(
            '<span class="error">' + text + '</span>');
        $(form).find(':input#' + name).parent().addClass('error');
    });
}

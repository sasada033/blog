$(function() {
    $('.description').each(function(i) {
        var str = $(this).html().replace(/#+/g, '');
        $(this).html(str);
    });
});

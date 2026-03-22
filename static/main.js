$(document).ready(function () {

    // Register validation
    $('#registerForm').submit(function (e) {
        var ok = true;
        if ($('#username').val().trim() == '') { $('#username').addClass('is-invalid'); ok = false; }
        if ($('#email').val().trim() == '')    { $('#email').addClass('is-invalid'); ok = false; }
        if ($('#password').val().length < 4)   { $('#password').addClass('is-invalid'); ok = false; }
        if (!ok) e.preventDefault();
    });

    // Login validation
    $('#loginForm').submit(function (e) {
        var ok = true;
        if ($('#email').val().trim() == '')    { $('#email').addClass('is-invalid'); ok = false; }
        if ($('#password').val().trim() == '') { $('#password').addClass('is-invalid'); ok = false; }
        if (!ok) e.preventDefault();
    });

    // Capsule form validation
    $('#capsuleForm').submit(function (e) {
        var ok = true;
        if ($('#title').val().trim() == '')   { $('#title').addClass('is-invalid'); ok = false; }
        if ($('#message').val().trim() == '') { $('#message').addClass('is-invalid'); ok = false; }
        if ($('#unlock_date').val() == '')    { $('#unlock_date').addClass('is-invalid'); ok = false; }
        if (!ok) e.preventDefault();
    });

    // Countdown timer
    function tick() {
        $('.countdown').each(function () {
            var diff = new Date($(this).data('unlock')) - new Date();
            if (diff <= 0) { $(this).text('Unlocking...'); return; }
            var d = Math.floor(diff / 86400000);
            var h = Math.floor((diff % 86400000) / 3600000);
            var m = Math.floor((diff % 3600000) / 60000);
            var s = Math.floor((diff % 60000) / 1000);
            $(this).text(d + 'd ' + h + 'h ' + m + 'm ' + s + 's left');
        });
    }
    tick();
    setInterval(tick, 1000);

    // Show capsule message on click
    $('.view-btn').click(function () {
        var id = $(this).data('id');
        $('#msg-' + id).slideToggle(300);
        $(this).text($(this).text() == 'View' ? 'Hide' : 'View');
    });

});

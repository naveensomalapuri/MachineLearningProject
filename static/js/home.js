$(document).ready(function () {
    // Check local storage for saved theme preference
    const savedTheme = localStorage.getItem('theme');

    //Apply saved theme or default to light mode
    if (savedTheme === 'dark') {
        $('#darkModeSwitch').prop('checked', true);
        $('body').addClass('dark-mode');
        $('nav').addClass('dark-mode');
        $('.navbar-brand span').addClass('dark-text');
        $('.form-container ').css('background-color', '#333'); 
    } else {
        $('body').removeClass('dark-mode');
        $('nav').removeClass('dark-mode');
        $('.form-container ').css('background-color', '#fff');
        $('.navbar-brand span').removeClass('dark-text');
     
    }

    // Toggle theme when the checkbox is clicked
    $('#darkModeSwitch').on('change', function () {
        if ($(this).is(':checked')) {
            $('body').addClass('dark-mode');
            $('nav').addClass('dark-mode');
            $('.form-container ').css('background-color', '#333');
            localStorage.setItem('theme', 'dark');
            $('.navbar-brand span').addClass('dark-text');
           
        } else {
            $('body').removeClass('dark-mode');
            $('.form-container ').css('background-color', '#fff');
            $('nav').removeClass('dark-mode');
            $('.navbar-brand span').removeClass('dark-text');
            localStorage.setItem('theme', 'light');
        }
    });
});


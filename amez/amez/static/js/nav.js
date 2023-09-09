document.addEventListener('DOMContentLoaded', function() {
    var navLinks = document.querySelectorAll('a.nav-link');

    for (var i = 0; i < navLinks.length; i++) {
        if(window.location.href == navLinks[i].getAttribute('href')) {
            navLinks[i].classList.add('active');
        }
    }
});
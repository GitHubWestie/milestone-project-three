document.addEventListener('DOMContentLoaded',
    function() {
        var sidenav = document.querySelectorAll('.sidenav');
        M.Sidenav.init(sidenav);
        var elems = document.querySelectorAll('select');
        M.FormSelect.init(elems);
        var elems = document.querySelectorAll('.modal');
        M.Modal.init(elems);
    });
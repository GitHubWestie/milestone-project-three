document.addEventListener('DOMContentLoaded',
    function() {
        var sidenav = document.querySelectorAll('.sidenav');
        M.Sidenav.init(sidenav);
        var elems = document.querySelectorAll('select');
        M.FormSelect.init(elems);
        var elems = document.querySelectorAll('.modal');
        M.Modal.init(elems);

        const selectDropdowns = document.querySelectorAll('.select-dropdown.dropdown-trigger');

        // Loop through each select-dropdown and add an id or name attribute
        selectDropdowns.forEach((dropdown, index) => {
          dropdown.setAttribute('id', `select-dropdown-${index}`);
          dropdown.setAttribute('name', `select-dropdown-${index}`);
          dropdown.setAttribute('label', `select-dropdown-${index}`);
        });
    });
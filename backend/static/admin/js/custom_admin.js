document.addEventListener('DOMContentLoaded', function() {
    var sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;

    var searchDiv = document.createElement('div');
    searchDiv.className = 'sidebar-search-form';
    searchDiv.innerHTML = '<form onsubmit="return false;">' +
        '<div class="input-group">' +
        '<input class="form-control" type="search" placeholder="Search..." autocomplete="off" id="sidebar-search-input">' +
        '<div class="input-group-append">' +
        '<button class="btn" type="button"><i class="fas fa-search"></i></button>' +
        '</div></div></form>';

    var userPanel = sidebar.querySelector('.user-panel');
    if (userPanel) {
        sidebar.insertBefore(searchDiv, userPanel);
    } else {
        sidebar.insertBefore(searchDiv, sidebar.firstChild);
    }

    var searchInput = document.getElementById('sidebar-search-input');
    searchInput.addEventListener('input', function() {
        var query = this.value.toLowerCase().trim();
        var headers = document.querySelectorAll('.nav-sidebar > .nav-item > .nav-header');

        headers.forEach(function(headerEl) {
            var headerLi = headerEl.closest('.nav-item') || headerEl.parentElement;
            var sibling = headerLi.nextElementSibling;
            var hasVisible = false;

            while (sibling && !sibling.querySelector('.nav-header')) {
                var text = sibling.textContent.toLowerCase();
                if (!query || text.indexOf(query) !== -1) {
                    sibling.style.display = '';
                    hasVisible = true;
                } else {
                    sibling.style.display = 'none';
                }
                sibling = sibling.nextElementSibling;
            }
            headerLi.style.display = (!query || hasVisible) ? '' : 'none';
        });

        // Also handle nav items that are not preceded by headers (like Dashboard)
        var allItems = document.querySelectorAll('.nav-sidebar > .nav-item');
        allItems.forEach(function(item) {
            if (!item.querySelector('.nav-header') && item.style.display !== 'none') {
                var text = item.textContent.toLowerCase();
                if (query && text.indexOf(query) === -1) {
                    item.style.display = 'none';
                } else if (!query) {
                    item.style.display = '';
                }
            }
        });
    });

    // Mobile sidebar toggle (since navbar is hidden)
    if (window.innerWidth <= 991) {
        var toggle = document.createElement('button');
        toggle.innerHTML = '<i class="fas fa-bars"></i>';
        toggle.style.cssText = 'position:fixed;top:15px;left:15px;z-index:1050;background:#1e3a5f;color:#fff;border:none;border-radius:6px;padding:10px 14px;font-size:16px;box-shadow:0 2px 10px rgba(0,0,0,0.3);cursor:pointer;';
        toggle.addEventListener('click', function() {
            document.body.classList.toggle('sidebar-open');
        });
        document.body.appendChild(toggle);
    }
});

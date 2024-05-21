document.getElementById('production-plan').addEventListener('click', function() {
    var subMenu = document.querySelector('.sub-menu');
    subMenu.classList.toggle('active');
});

document.getElementById('show-plan').addEventListener('click', function() {
    setActiveState(this);
});

document.getElementById('update-plan').addEventListener('click', function() {
    setActiveState(this);
});

document.getElementById('add-plan').addEventListener('click', function() {
    setActiveState(this);
});

function setActiveState(element) {
    var menuItems = document.querySelectorAll('.sub-menu .menu-item');
    menuItems.forEach(function(item) {
        item.classList.remove('active');
    });
    element.classList.add('active');
}

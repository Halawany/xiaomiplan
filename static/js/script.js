document.getElementById('insert-plan').addEventListener('click', function() {
    // Add logic for inserting plan
    // Example: window.location.href = '/insert-plan';
    setActiveState(this);
});

document.getElementById('update-plan').addEventListener('click', function() {
    // Add logic for updating plan
    // Example: window.location.href = '/update-plan';
    setActiveState(this);
});

document.getElementById('show-plan').addEventListener('click', function() {
    // Add logic for showing plan
    // Example: window.location.href = '/show-plan';
    setActiveState(this);
});

function setActiveState(element) {
    var menuItems = document.getElementsByClassName('menu-item');
    for (var i = 0; i < menuItems.length; i++) {
        menuItems[i].classList.remove('active');
    }
    element.classList.add('active');

    // // Update greeting message with username
    // var username = "John Doe"; // Replace with actual username from Django
    // document.getElementById('username').innerText = username;
}

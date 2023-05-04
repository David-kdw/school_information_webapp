// Get the navigation menu and the links
var nav = document.querySelector('nav');
var links = document.querySelectorAll('nav ul li a');

// Add an active class to the current link in the navigation menu
function setActiveLink() {
  // Get the current URL
  var currentUrl = window.location.href;

  // Loop through the links and check if their href attribute matches the current URL
  for (var i = 0; i < links.length; i++) {
    var link = links[i];
    if (link.href === currentUrl) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  }
}

// Call the setActiveLink function when the page is loaded and when the navigation menu is clicked
window.addEventListener('load', setActiveLink);
nav.addEventListener('click', setActiveLink);

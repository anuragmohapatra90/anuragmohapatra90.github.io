// Function to handle the interactive year tabs on the publications page
function showYear(buttonElement, year) {
  // Hide all publication panels
  var allPanels = document.querySelectorAll('.pub-panel');
  allPanels.forEach(function(panel) {
    panel.style.display = 'none';
  });

  // Deactivate all buttons
  var allButtons = document.querySelectorAll('.year-button');
  allButtons.forEach(function(btn) {
    btn.classList.remove('active');
  });

  // Show the target panel and activate the clicked button
  var targetPanel = document.getElementById('panel-' + year);
  if (targetPanel) {
    targetPanel.style.display = 'block';
  }
  buttonElement.classList.add('active');
}


// This single function runs after the entire page is loaded
document.addEventListener('DOMContentLoaded', function() {
  
  // --- Logic for the Publications Page Year Tabs ---
  var firstPubButton = document.querySelector('.year-button');
  if (firstPubButton) {
    firstPubButton.click(); // Automatically "click" the first year button
  }

  // --- Logic for the Navigation Bar External Links ---
  var navLinks = document.querySelectorAll('.masthead__menu-item a');
  navLinks.forEach(function(link) {
    // Check if the link is external
    if (link.href && !link.href.startsWith(window.location.origin) && !link.href.startsWith('/')) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer'); // Important for security
    }
  });

});
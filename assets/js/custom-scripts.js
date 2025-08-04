// Function to handle the interactive year tabs on the publications page
function showYear(buttonElement, year) {
  var allPanels = document.querySelectorAll('.pub-panel');
  allPanels.forEach(function(panel) {
    panel.style.display = 'none';
  });

  var allButtons = document.querySelectorAll('.year-button');
  allButtons.forEach(function(btn) {
    btn.classList.remove('active');
  });

  var targetPanel = document.getElementById('panel-' + year);
  if (targetPanel) {
    targetPanel.style.display = 'block';
  }
  buttonElement.classList.add('active');
}

// This single function runs after the entire page is loaded
document.addEventListener('DOMContentLoaded', function() {
  
  // Logic for the Publications Page Year Tabs
  var firstPubButton = document.querySelector('.year-button');
  if (firstPubButton) {
    firstPubButton.click();
  }

  // --- DEFINITIVE FIX for Navigation Bar External Links ---
  // We add a small delay to ensure the menu is built before our script runs.
  setTimeout(function() {
    var navLinks = document.querySelectorAll('.masthead__menu-item a');
    navLinks.forEach(function(link) {
      if (link.href && link.href.includes('http')) { // A simpler check for any external link
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
      }
    });
  }, 500); // 500ms delay

});
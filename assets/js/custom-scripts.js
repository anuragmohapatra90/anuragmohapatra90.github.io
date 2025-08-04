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
  // This waits a brief moment to ensure the whole page, including the navigation, is fully built.
  setTimeout(function() {
    var navLinks = document.querySelectorAll('.masthead__menu-item a');
    navLinks.forEach(function(link) {
      // A simple check to see if a link is external
      if (link.href && (link.href.startsWith('http://') || link.href.startsWith('https://')) && !link.href.includes('anuragmohapatra90.github.io')) {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer'); // Important for security
      }
    });
  }, 500); // 500ms delay

});
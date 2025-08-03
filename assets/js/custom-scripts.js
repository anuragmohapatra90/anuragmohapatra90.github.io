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

// This function runs after the entire page is loaded
document.addEventListener('DOMContentLoaded', function() {
  // Automatically "click" the first year button to show its content by default
  var firstButton = document.querySelector('.year-button');
  if (firstButton) {
    firstButton.click();
  }
});
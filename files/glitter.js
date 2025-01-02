window.onload = function() {
  const body = document.body;
  const checkbox = document.getElementById('toggle-background');
  const glitterEnabled = localStorage.getItem('glitterBackground') === 'true';
  
  // Apply saved background state
  if (glitterEnabled) {
    body.style.backgroundImage = "url('/images/glitter.gif')";
    body.style.backgroundSize = "auto";
    body.style.backgroundRepeat = "repeat";
    checkbox.checked = true;
  }
};

// Save state to localStorage and apply background
function toggleBackground() {
  const body = document.body;
  const checkbox = document.getElementById('toggle-background');
  const glitterEnabled = checkbox.checked;

  // Save state
  localStorage.setItem('glitterBackground', glitterEnabled);

  // Apply or remove background
  if (glitterEnabled) {
    body.style.backgroundImage = "url('/images/glitter.gif')";
    body.style.backgroundSize = "auto";
    body.style.backgroundRepeat = "repeat";
  } else {
    body.style.backgroundImage = "none";
  }
}
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
    // Change link colors above first hr
    const linksAbove = document.querySelectorAll('h1 + p .link');
    linksAbove.forEach(link => link.style.color = '#2f8aee');
    // Change "Hey!" color
    const hey = document.querySelector('h1 strong');
    if (hey) hey.style.color = '#ffffff';
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
    // Change link colors above first hr
    const linksAbove = document.querySelectorAll('h1 + p .link');
    linksAbove.forEach(link => link.style.color = '#2f8aee');
    // Change "Hey!" color
    const hey = document.querySelector('h1 strong');
    if (hey) hey.style.color = '#ffffff';
  } else {
    body.style.backgroundImage = "none";
    // Reset link colors above first hr
    const linksAbove = document.querySelectorAll('h1 + p .link');
    linksAbove.forEach(link => link.style.color = '');
    // Reset "Hey!" color
    const hey = document.querySelector('h1 strong');
    if (hey) hey.style.color = '';
  }
}
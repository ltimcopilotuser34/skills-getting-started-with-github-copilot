// Load activities when the page loads
document.addEventListener('DOMContentLoaded', () => {
  loadActivities();
});

// Fetch and display activities
async function loadActivities() {
  try {
    const response = await fetch('/activities');
    const activities = await response.json();
    
    displayActivities(activities);
    populateActivitySelect(activities);
  } catch (error) {
    console.error('Error loading activities:', error);
    document.getElementById('activities-list').innerHTML = 
      '<p class="error">Failed to load activities. Please try again later.</p>';
  }
}

// Display activities in cards
function displayActivities(activities) {
  const container = document.getElementById('activities-list');
  container.innerHTML = '';
  
  for (const [name, details] of Object.entries(activities)) {
    const card = document.createElement('div');
    card.className = 'activity-card';
    
    const participantsList = details.participants.length > 0
      ? `<ul>${details.participants.map(email => `<li>${email}</li>`).join('')}</ul>`
      : '<p class="no-participants">No participants yet</p>';
    
    card.innerHTML = `
      <h4>${name}</h4>
      <p><strong>Description:</strong> ${details.description}</p>
      <p><strong>Schedule:</strong> ${details.schedule}</p>
      <p><strong>Capacity:</strong> ${details.participants.length}/${details.max_participants}</p>
      <div class="participants">
        <h5>Current Participants:</h5>
        ${participantsList}
      </div>
    `;
    
    container.appendChild(card);
  }
}

// Populate the activity dropdown
function populateActivitySelect(activities) {
  const select = document.getElementById('activity');
  
  for (const name of Object.keys(activities)) {
    const option = document.createElement('option');
    option.value = name;
    option.textContent = name;
    select.appendChild(option);
  }
}

// Handle form submission
document.getElementById('signup-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const email = document.getElementById('email').value;
  const activity = document.getElementById('activity').value;
  const messageDiv = document.getElementById('message');
  
  try {
    const response = await fetch(`/activities/${encodeURIComponent(activity)}/signup?email=${encodeURIComponent(email)}`, {
      method: 'POST',
    });
    
    const data = await response.json();
    
    if (response.ok) {
      messageDiv.className = 'message success';
      messageDiv.textContent = data.message;
      messageDiv.classList.remove('hidden');
      
      // Reload activities to show updated participant list
      await loadActivities();
      
      // Reset form
      document.getElementById('signup-form').reset();
    } else {
      throw new Error(data.detail || 'Failed to sign up');
    }
  } catch (error) {
    messageDiv.className = 'message error';
    messageDiv.textContent = error.message;
    messageDiv.classList.remove('hidden');
  }
  
  // Hide message after 5 seconds
  setTimeout(() => {
    messageDiv.classList.add('hidden');
  }, 5000);
});

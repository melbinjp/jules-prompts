// The booking page. The times appear only once every field is filled in.
const form = document.getElementById('book');
const times = document.querySelector('.times');

form.addEventListener('input', () => {
  const filled = [...form.querySelectorAll('input[required]')].every(i => i.value.trim());
  if (filled && times.hidden) { times.hidden = false; loadSlots(); }
});

async function loadSlots() {
  const slots = await (await fetch('/slots')).json();
  document.getElementById('slots').innerHTML = slots
    .map(s => `<button type="button" class="time" data-id="${s.id}">${s.label}</button>`).join('');
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  // The clinic's rule: at most two upcoming appointments per patient.
  const mine = await (await fetch('/bookings?phone=' + encodeURIComponent(form.phone.value))).json();
  if (mine.length >= 2) { show('You already have two appointments booked.'); return; }
  const chosen = document.querySelector('.time[aria-pressed="true"]');
  const response = await fetch('/bookings', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ ...Object.fromEntries(new FormData(form)), slot: chosen.dataset.id }),
  });
  show(response.ok ? 'Booked.' : messageFor(response.status));
});

function show(text) { document.getElementById('message').textContent = text; }

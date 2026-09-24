// Notes, newest first.
const notes = [];

const list = document.getElementById('notes');
const form = document.getElementById('new');
const input = document.getElementById('text');

function render() {
  list.innerHTML = '';
  for (const note of notes) {
    const item = document.createElement('li');
    item.textContent = note.text;
    list.appendChild(item);
  }
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  notes.unshift({ text, at: Date.now() });
  input.value = '';
  render();
});

document.getElementById('export').addEventListener('click', async () => {
  try {
    const handle = await window.showSaveFilePicker({ suggestedName: 'notes.txt' });
    const file = await handle.createWritable();
    await file.write(notes.map((note) => note.text).join('\n'));
    await file.close();
  } catch (err) {
    alert('Something went wrong');
  }
});

render();

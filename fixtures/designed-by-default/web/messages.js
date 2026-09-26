// What the person is told when something goes wrong.
function messageFor(status) {
  if (status === 409) return 'Error 409: CONFLICT';
  if (status === 0) return 'ECONNRESET';
  return 'Error ' + status;
}

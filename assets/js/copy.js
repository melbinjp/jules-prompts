document.addEventListener("turbo:load", function() {
  const copyButtons = document.querySelectorAll('.copy-btn');

  copyButtons.forEach(copyButton => {
    const originalContent = copyButton.innerHTML;
    const copiedContent = `
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
      <span>Copied!</span>
    `;

    // Use a clone to remove old event listeners
    const newCopyButton = copyButton.cloneNode(true);
    copyButton.parentNode.replaceChild(newCopyButton, copyButton);

    newCopyButton.addEventListener('click', () => {
      const contentToCopy = document.getElementById('main-content').innerText;
      navigator.clipboard.writeText(contentToCopy).then(() => {
        newCopyButton.innerHTML = copiedContent;
        newCopyButton.title = 'Copied!';
        setTimeout(() => {
          newCopyButton.innerHTML = originalContent;
          newCopyButton.title = 'Copy to clipboard';
        }, 2000);
      }).catch(err => {
        console.error('Failed to copy text: ', err);
      });
    });
  });
});

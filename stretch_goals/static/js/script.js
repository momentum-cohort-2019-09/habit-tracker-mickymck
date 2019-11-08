
for (let button of document.querySelectorAll('.record-submit-button')) {
    button.addEventListener('submit', event => {
        fetch(`/api/records/`, {
            method = 'POST',
        })
    })
}

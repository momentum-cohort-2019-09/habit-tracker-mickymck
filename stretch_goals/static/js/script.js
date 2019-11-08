

for (let form of document.querySelectorAll('.record-form')) {
    form.addEventListener('submit', event => {
        event.preventDefault()
        fetch(`/${form.dataset.goalPk}/add_record`, {
            method: 'POST',
            body: new FormData(form)
        }).then(res => res.json())
        .then(data => {
            if(data.ok) {
                // Asynchronously rerender hompage 
                // Remove number and maybe show that it was logged
                alert('good')
            } else {
                alert("no good")
            }
        })
    })
}

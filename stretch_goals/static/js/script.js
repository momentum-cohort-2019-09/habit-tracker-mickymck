

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



for (let button of document.querySelectorAll('.edit-record-button')) {
    button.addEventListener('click', event => {
        event.preventDefault()
        button.parentElement.querySelector('.hidden-actual-number').style.display = 'none'
        button.parentElement.querySelector('.hidden-record-form').style.display = 'inline-block'
    })
}


for (let form of document.querySelectorAll('.hidden-record-form')) {
    form.addEventListener('submit', event => {
        event.preventDefault()
        fetch(`/${form.dataset.recordPk}/edit_record`, {
            method: 'POST',
            body: new FormData(form)
        })
        .then(res => res.json())
        .then(data => {
            if(data.ok) {
                alert('good')
            } else {
                alert("no good")
            }
        })
    })
}



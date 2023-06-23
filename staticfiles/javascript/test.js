const seats = document.querySelectorAll(".seat")
const results = document.querySelector('.results')
const resultsBtn = document.querySelector('.send-results')
const alertMsg = document.querySelector('.alert-msg')
const closeBtn = document.querySelector('.closeAlertBtn')
const RstBtn = document.querySelector('.RstBtn')

let reservedSeats = []

function displayResult() {
    results.innerHTML = ""
    reservedSeats.forEach(seat => {
        results.innerHTML += `<p>row: ${seat.row}, seat: ${seat.seat}, pk: ${seat.pk}</p>`
    })
    let pks = []
    reservedSeats.forEach(seat => {
        pks.push(seat.pk * 1)
    })
    resultsBtn.value = pks.join(", ")
}

seats.forEach(x =>
    x.addEventListener('click', (e) => {
        let seat = e.currentTarget;
        if (seat.className.includes('taken-seat')) {
            alertMsg.hidden = false;
            // alert('seat is taken')
        } else if (seat.className.includes('free-seat')) {
            seat.classList.remove('free-seat')
            seat.classList.add('reserved-seat')
            reservedSeats.push({'pk': seat.dataset.pk, 'row': seat.dataset.row, 'seat': seat.dataset.seat})
            displayResult()
        } else if (seat.className.includes('reserved-seat')) {
            seat.classList.remove('reserved-seat')
            seat.classList.add('free-seat')
            reservedSeats = reservedSeats.filter(y => y.pk !== seat.dataset.pk)
            displayResult()
        }
    })
)
document.addEventListener('click', () => {
    if (alertMsg.hidden === false) {
        setTimeout(() => {
            alertMsg.hidden = true
        }, 2000)
    }
})

closeBtn.addEventListener('click', (e) => {
    e.currentTarget.parentElement.hidden = true
})

RstBtn.addEventListener('click', () => {
    resultsBtn.value = "";
    reservedSeats = [];
    results.innerHTML = "";
    seats.forEach(seat => {
        if (seat.className.includes('reserved-seat')) {
            seat.classList.remove('reserved-seat')
            seat.classList.add('free-seat')
        }

    })
})
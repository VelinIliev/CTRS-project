const seats = document.querySelectorAll(".seat");
const results = document.querySelector('.results');
const resultsBtn = document.querySelector('.send-results');
const alertMsg = document.querySelector('.alert-msg');
const closeBtn = document.querySelector('.closeAlertBtn');
const RstBtn = document.querySelector('.RstBtn');
const id_reserved_seats = document.querySelector('#id_reserved_seats');
const FinishBtn = document.querySelector('.FinishBtn');
const ConfirmBtn = document.querySelector('.ConfirmBtn');
const numberOfTicketsReserved = document.querySelector('.numberOfTicketsReserved');
const id_is_finished = document.querySelector('#id_is_finished')

FinishBtn.style.display = "none";
results.innerHTML = "";

let reservedSeats = [];
let leavePage = false;

function displayResult() {
    results.innerHTML = "";
    id_reserved_seats.value = "";
    let pks = [];
    let seats = []
    reservedSeats.forEach(seat => {
        pks.push(seat.pk * 1);
        seats.push(`R${seat.row}-S${seat.seat}`);
    })
    id_reserved_seats.value = pks.join(", ");
    results.innerHTML = seats.join(", ")

}

function reservation(e) {
    let seat = e.currentTarget;
    if (seat.className.includes('taken-seat')) {
        alertMsg.querySelector('strong').textContent = `The seat is already taken.`;
        alertMsg.hidden = false;
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
}

seats.forEach(seat =>
    seat.addEventListener('click', reservation)
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
    // resultsBtn.value = "";
    reservedSeats = [];
    results.innerHTML = "";
    id_reserved_seats.value = '';
    seats.forEach(seat => {
        if (seat.className.includes('reserved-seat')) {
            seat.classList.remove('reserved-seat')
            seat.classList.add('free-seat')
        }

    });

})

ConfirmBtn.addEventListener('click', () => {
    if (reservedSeats.length === numberOfTicketsReserved.textContent * 1) {
        id_is_finished.checked = true;
        // console.log(`ffff${id_is_finished}`)
        ConfirmBtn.style.display = 'none';
        RstBtn.style.display = 'none';
        FinishBtn.style.display = 'inline-block';
        seats.forEach(seat => {
            seat.removeEventListener('click', reservation)
        })
    } else if (reservedSeats.length < numberOfTicketsReserved.textContent * 1) {
        let seatsToReserve = numberOfTicketsReserved.textContent * 1 - reservedSeats.length;
        alertMsg.querySelector('strong').textContent = `You must mark ${seatsToReserve} more seats.`;
        alertMsg.hidden = false;
    } else if (reservedSeats.length > numberOfTicketsReserved.textContent * 1) {
        let seatsToReserve = reservedSeats.length - numberOfTicketsReserved.textContent * 1;
        alertMsg.querySelector('strong').textContent = `You reserved ${seatsToReserve} extra seats.`;
        alertMsg.hidden = false;
    }
})
FinishBtn.addEventListener('click', (event) => {
    leavePage = true;
});

window.onbeforeunload = function (e) {
    if (leavePage) {
        console.log('xxx')
    } else {
        e.preventDefault();
        e.returnValue = 'Are you sure you want to leave this page?';
        console.log('yyy')
    }
}
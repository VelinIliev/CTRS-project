const seats = document.querySelectorAll(".seat")
const results = document.querySelector('.results')
const resultsBtn = document.querySelector('.send-results')
const inResults = document.querySelector('.input-results')

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
    inResults.value = pks.join(", ")
    resultsBtn.value = pks.join(", ")
}

seats.forEach(x =>
    x.addEventListener('click', (e) => {
        seat = e.currentTarget;
        // console.log(e.currentTarget.dataset.pk);
        if (seat.className.includes('taken-seat')) {
            console.log('OK')
        } else if (seat.className.includes('free-seat')) {
            // console.log(seat.dataset.pk)
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

// function getCookie(name) {
//     if (!document.cookie) {
//         return null;
//     }
//
//     const xsrfCookies = document.cookie.split(';')
//         .map(c => c.trim())
//         .filter(c => c.startsWith(name + '='));
//
//     if (xsrfCookies.length === 0) {
//         return null;
//     }
//     return decodeURIComponent(xsrfCookies[0].split('=')[1]);
// }

// resultsBtn.addEventListener('click', () => {
//     const csrfToken = getCookie('csrftoken');
//
//     const headers = new Headers({
//         'Content-Type': 'x-www-form-urlencoded',
//         'csrftoken': csrfToken
//     });
//     fetch('http://127.0.0.1:8000/projection/reservations/', {
//         method: "POST",
//         headers,
//         body: JSON.stringify({
//             "values": reservedSeats,
//         }),
//     })
//         // .then(data => loadData())
//         .catch((error) => console.log(error))
// })
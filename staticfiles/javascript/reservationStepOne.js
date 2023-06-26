const numberInput = document.querySelectorAll('.numberInput');
const id_type_of_tickets = document.querySelector('#id_type_of_tickets');
const id_number_of_tickets = document.querySelector('#id_number_of_tickets');
const id_total_price = document.querySelector('#id_total_price');
const displayResult = document.querySelector('.display-result')

// let total = 0;
// let numberOfTickets = 0;
// let typeOfTickets = 'test'
let statistic = {}

numberInput.forEach(el => {
        let typeTicket = el.parentElement.parentElement.className;
        let price = el.parentElement.textContent.trim() * 1;
        let number = el.value * 1
        if (!(typeTicket in statistic)) {
            statistic[typeTicket] = {'number': number, 'price': price}
        }
        el.addEventListener('change', (e) => {
            // console.log(e.currentTarget.value)
            displayResult.innerHTML = ``
            statistic[e.currentTarget.parentElement.parentElement.className]['number'] = e.currentTarget.value * 1;
            let total = 0;
            let numberOfTickets = 0;
            let tickets = ''
            for (const [typeTicket, value] of Object.entries(statistic)) {
                if (value.number !== 0) {
                    total += value.number * value.price;
                    numberOfTickets += value.number
                    tickets += `${typeTicket},${value.number},${value.price};`
                    displayResult.innerHTML += `<p>${typeTicket} ${value.number}</p>`
                }
            }
            id_total_price.value = total;
            id_number_of_tickets.value = numberOfTickets;
            id_type_of_tickets.value = tickets;
        })
    }
)



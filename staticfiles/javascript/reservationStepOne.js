const numberInput = document.querySelectorAll('.numberInput');
const id_type_of_tickets = document.querySelector('#id_type_of_tickets');
const id_number_of_tickets = document.querySelector('#id_number_of_tickets');
const id_total_price = document.querySelector('#id_total_price');
const displayResult = document.querySelector('.display-result')

let statistic = {}

numberInput.forEach(el => {
        let typeTicket = el.parentElement.querySelector('div:first-child').className;
        let price = el.parentElement.querySelector('.price-value').textContent.trim() * 1;
        let number = el.value * 1
        if (!(typeTicket in statistic)) {
            statistic[typeTicket] = {'number': number, 'price': price}
        }
        console.log(statistic)
        el.addEventListener('change', (e) => {

            displayResult.innerHTML = ``
            statistic[typeTicket]['number'] = e.currentTarget.value * 1;
            let total = 0;
            let numberOfTickets = 0;
            let tickets = ''
            for (const [typeTicket, value] of Object.entries(statistic)) {
                if (value.number !== 0) {
                    total += value.number * value.price;
                    numberOfTickets += value.number
                    tickets += `${typeTicket},${value.number},${value.price};`
                }
            }
            displayResult.innerHTML += `<p>Total: $${total.toFixed(2)}`
            id_total_price.value = total.toFixed(2);
            id_number_of_tickets.value = numberOfTickets;
            id_type_of_tickets.value = tickets;
        })
    }
)



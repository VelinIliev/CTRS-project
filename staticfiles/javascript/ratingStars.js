const stars = document.querySelectorAll('.vote')
const starInput = document.querySelector('#id_rating')
const ratingWrap = document.querySelector('.rating-wrap')


function createStars(star, i) {
    let divEl = document.createElement("DIV");
    divEl.className = 'rating-star vote';
    divEl.dataset.starn = `${i}`;
    ratingWrap.appendChild(divEl);
    divEl.addEventListener('click', e => {
        starInput.value = '';
        let numberOfStars = e.currentTarget.dataset.starn * 1;
        starInput.value = numberOfStars;
        displayStars(numberOfStars)
    })
    imgEl = document.createElement("IMG")
    imgEl.src = `/static/images/stars/star${star}.svg`
    imgEl.alt = "star"
    divEl.appendChild(imgEl)
}

function displayStars(numberOfStars) {
    ratingWrap.innerHTML = ''
    for (let i = 1; i <= 10; i++) {
        if (i <= numberOfStars) {
            createStars('10', i)
        } else {
            createStars('00', i)
        }
    }

}


stars.forEach(star => {
        star.addEventListener('click', (e) => {
            starInput.value = '';
            let numberOfStars = e.currentTarget.dataset.starn * 1;
            starInput.value = numberOfStars;
            displayStars(numberOfStars)
        })

    }
)

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
    divEl.addEventListener('mouseover', e => {
        starInput.value = '';
        let numberOfStars = e.currentTarget.dataset.starn * 1;
        starInput.value = numberOfStars;
        displayStars(numberOfStars)
    })

    let imgSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    imgSvg.setAttribute('fill', `${star}`);
    imgSvg.setAttribute('viewBox', '0 0 200 200');
    imgSvg.setAttribute('stroke', 'none');
    imgSvg.setAttribute('x', '0px');
    imgSvg.setAttribute('y', '0px');
    imgSvg.innerHTML = `
    <g>
        <path class="st0" d="M106.8,4.2l25,50.7c1.1,2.2,3.2,3.8,5.7,4.2l56,8.1c6.2,0.9,8.7,8.6,4.2,12.9l-40.5,39.5
        c-1.8,1.7-2.6,4.3-2.2,6.7l9.6,55.7c1.1,6.2-5.4,10.9-11,8l-50-26.3c-2.2-1.2-4.9-1.2-7.1,0l-50,26.3c-5.6,2.9-12.1-1.8-11-8
        l9.6-55.7c0.4-2.5-0.4-5-2.2-6.7L2.3,80.2c-4.5-4.4-2-12,4.2-12.9l56-8.1c2.5-0.4,4.6-1.9,5.7-4.2l25-50.7
        C96-1.4,104-1.4,106.8,4.2z"/>
    </g>
    `
    divEl.appendChild(imgSvg)
}


function displayStars(numberOfStars) {
    ratingWrap.innerHTML = ''
    for (let i = 1; i <= 10; i++) {
        if (i <= numberOfStars) {
            createStars('#FFCC00', i)
        } else {
            createStars('#DDDDDD', i)
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
stars.forEach(star => {
        star.addEventListener('mouseover', (e) => {
            starInput.value = '';
            let numberOfStars = e.currentTarget.dataset.starn * 1;
            starInput.value = numberOfStars;
            displayStars(numberOfStars)
        })
    }
)

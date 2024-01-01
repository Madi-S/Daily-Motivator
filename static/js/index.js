// Get HTML elements
const quoteHeading = document.getElementById('quote')
const authorHeading = document.getElementById('author')
const divSections = document.querySelectorAll('.section-b__row')

// Set random main quote and author
quoteHeading.textContent = getRandom(quotes)
authorHeading.textContent = getRandom(authors) + ':'

// Arrange quotes in three rows
for (let i = 0; i < quotes.length; i += 3) {
    console.log(quotes[i])
    divSections[0].insertAdjacentHTML('beforeend', `<p>${quotes[i]}</p>`)
    if (i + 1 < quotes.length)
        divSections[1].insertAdjacentHTML(
            'beforeend',
            `<p>${quotes[i + 1]}</p>`
        )
    if (i + 2 < quotes.length)
        divSections[2].insertAdjacentHTML(
            'beforeend',
            `<p>${quotes[i + 2]}</p>`
        )
}

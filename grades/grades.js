async function getGrades() {
    const response = await fetch("https://raw.githubusercontent.com/kaenovsky/iftsnotes/main/grades/grades.json");
    const data = await response.json();    
    const arrGrades = data.Grades;
    let sumGrades = 0;
    let totalGrades = 0;    

    const container = document.querySelector('.grades-container');
    
    for (let i of arrGrades) {        
        
        // create card element
        const newCard = document.createElement('div');
        newCard.classList.add('card');
    
        // create div container for title and grade
        const newDiv = document.createElement('div');        
        
        // create title for card
        const newTitle = document.createElement('p');
        newTitle.classList.add('title');
        newTitle.innerText = `${i.code} - ${i.name}`;
        newDiv.appendChild(newTitle);
    
        // create grade element with grade
        const newGrade = document.createElement('p');
        newGrade.classList.add('grade');
        
        if (i.grade != null) {
            totalGrades = totalGrades + 1;
            sumGrades = sumGrades + i.grade;
            newGrade.innerText = `Nota final: ${i.grade}`;
        }

        newDiv.appendChild(newGrade);
    
        // set status
        const newStatus = document.createElement('div');
        newStatus.classList.add('status');
        newCard.classList.add('toggle-content', 'is-visible');

        if (i.status === 'Aprobada') {
            newCard.classList.add('green', 'isApproved');
            newStatus.innerText = i.status + "  🚀";
        } else {
            newCard.classList.add('grey', 'isPending');
            newStatus.innerText = i.status + "  👀";
        }
    
        // add elements to card
        newCard.appendChild(newDiv);
        newCard.appendChild(newStatus);
    
        // add card to markup
        container.appendChild(newCard);
    }

    // show average
    const avg = sumGrades / totalGrades;
    document.querySelector('#average').innerText = avg.toFixed(2);

    // show progress status
    const progressNum = Math.floor(totalGrades * 100 / arrGrades.length);
    console.log(`Cantidad de materias aprobadas: ${totalGrades} materias`);
    console.log(`Cantidad de materias de la carrera: ${arrGrades.length} materias`);
    console.log(`Por lo tanto, el porcentaje de progreso de la carrera es: ${progressNum}%`);

    // add progress number to markup
    const progressBar = document.querySelector('#progressBar');
    const progressNumSpan = document.querySelector('#progressNum');
    progressBar.value = progressNum;
    progressNumSpan.innerText = `${progressNum}%`;

}

getGrades();

// Toggle element visibility
const toggle = function (elem) {
    console.log(elem)
    for (let i of elem) {
        i.classList.toggle('is-visible');
    }
};

// Listen for click events (approved)
document.addEventListener('click', function (event) {

	// Make sure clicked element is our toggle
	if (!event.target.classList.contains('toggleA')) return;

	// Get the content
	let cardsA = document.querySelectorAll('.isApproved');
    console.log(cardsA)
	if (!cardsA) return;

	// Toggle the content
	toggle(cardsA);

}, false);

// Listen for click events (pending)
document.addEventListener('click', function (event) {

	// Make sure clicked element is our toggle
	if (!event.target.classList.contains('toggleP')) return;

	// Get the content
	let cardsP = document.querySelectorAll('.isPending');
    console.log(cardsP)
	if (!cardsP) return;

	// Toggle the content
	toggle(cardsP);

}, false);
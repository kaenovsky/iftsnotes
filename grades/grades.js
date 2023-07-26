async function getGrades() {
    const response = await fetch("https://raw.githubusercontent.com/kaenovsky/iftsnotes/main/grades/grades.json");
    const data = await response.json();    
    const arrGrades = data.Grades;

    const container = document.querySelector('.grades-container');
    
    for (let i of arrGrades) {
        
        // create card element
        const newCard = document.createElement('div');
        newCard.classList.add('card');
    
        // create title for card
        const newTitle = document.createElement('p');
        newTitle.classList.add('title');
        newTitle.innerText = i.name;
    
        // create grade element with grade
        const newGrade = document.createElement('p');
        newGrade.classList.add('grade');
        newGrade.innerText = `Nota final: ${i.grade}`;
    
        // set status (TBD toggle style)
        const newStatus = document.createElement('div');
        newStatus.classList.add('status');
        newStatus.innerText = i.status;
    
        // add elements to card
        newCard.appendChild(newTitle);
        newCard.appendChild(newGrade);
        newCard.appendChild(newStatus);
    
        // add card to markup
        container.appendChild(newCard);
    }
}

getGrades();
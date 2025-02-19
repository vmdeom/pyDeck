async function loadButtons(){
    
    let response = await fetch("/items");
    let buttons = await response.json();

    let container = document.getElementById("buttonContainer");

    container.innerHTML = "";

    let totalButtons = buttons.length;
    let emptyButtonsNeeded = 10 - totalButtons;

    createButtons(buttons, container);
    createEmptyButtons(emptyButtonsNeeded, container);

}

function createButtons(buttons, container){

    buttons.forEach(button => {
        let div = document.createElement("div");
        
        div.classList.add("deckButton");
        div.id = `btns_${button.id}`;
        div.dataset.action = button.effect_type;
        div.textContent = button.name;
        container.append(div);

       
        div.addEventListener("click", function(){
            console.log(this.dataset.action);
        })
    })
}

function createEmptyButtons(emptyButtonsNeeded, container){
    
    for(let i = 0; i < emptyButtonsNeeded; i++){
        let emptyButton = document.createElement("div");

        emptyButton.classList.add("deckButton", "emptyButton");
        emptyButton.textContent = "vazio";
        container.append(emptyButton);
    }
}

loadButtons();
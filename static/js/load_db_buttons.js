export function loadDBButtons(buttons, container){

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
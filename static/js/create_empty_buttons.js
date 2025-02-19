export function createEmptyButtons(emptyCount, container){

    for(let i = 0; i < emptyCount; i++){
        let emptyButton = document.createElement("div");

        emptyButton.classList.add("deckButton", "emptyButton");
        emptyButton.textContent = "empty";
        emptyButton.dataset.action = "this is empty"
        container.append(emptyButton);
        
        emptyButton.addEventListener("click", function(){
            console.log(this.dataset.action);
        })
    }
}
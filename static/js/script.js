/*function AddButton(){
    const deckButton = document.createElement("div");
    
}

function ClickButton(){
    return;
}

document.querySelectorAll(".deckButton").forEach(div => {
    div.addEventListener("click", function() {
        console.log({div: this.dataset.action});
    });
});
*/
async function loadButtons(){
    let response = await fetch("/items");
    let buttons = await response.json();

    let container = document.getElementById("buttonContainer");

    container.innerHTML = "";

    buttons.forEach(button => {
        let div = document.createElement("div");
        div.classList.add("deckButton");
        //div.id = `btns_${button.id}`;
        //div.dataset.action = button.effect_type;
        div.textContent = button.name;

        container.append(div);
    })


}

loadButtons();

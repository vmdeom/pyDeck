import { loadDBButtons } from "./load_db_buttons.js";
import { createEmptyButtons } from "./create_empty_buttons.js"

async function loadButtons(){
    
    let response = await fetch("/get_buttons");
    let buttons = await response.json();

    let container = document.getElementById("buttonContainer");

    container.innerHTML = "";

    let totalButtons = buttons.length;
    let emptyButtonsNeeded = 10 - totalButtons;
    
    loadDBButtons(buttons, container);
    createEmptyButtons(emptyButtonsNeeded, container);

}

loadButtons();

import { addDog } from "./add_dog.js";
import { loadDogList } from "./dog_list.js";

document.addEventListener('DOMContentLoaded', ()=> {
    console.log(" JS chargé !");


    const dogForm = document.getElementById('dog_form');

    dogForm.addEventListener('submit', (event)=>{
        event.preventDefault();
        console.log('empechage de refresh!') 
        addDog();
    });


    loadDogList();
    setInterval(loadDogList,10000)

});
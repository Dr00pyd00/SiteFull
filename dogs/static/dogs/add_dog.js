
import { loadDogList } from "./dog_list.js";

export function addDog() {

    
    console.log('Fonction ADD lancé !')

    // le token:
    const csrf_token = document.querySelector('meta[name="csrf_token"]').content;

    // le formulaire:
    const dogForm = document.getElementById('dog_form');


        // formdata? pour images:
        const formData = new FormData(dogForm);
        console.log('formData :')
        console.log(formData)

    fetch('http://127.0.0.1:8000/dogs/api_dog_list/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token
        },
        body: formData
    })


    .then(response => response.json())
    .then(data => {

        console.log(`dog added !`)
        loadDogList()
        dogForm.reset()

    });

}// fin funct



export function loadDogList() {

    const dogList = document.getElementById('dogs');

    const fragment = document.createDocumentFragment();


    fetch('http://127.0.0.1:8000/dogs/api_dog_list/')
    .then(response => response.json())
    .then(data => {

        // reset avant de recharger:
        dogList.innerHTML = '';

        data.forEach(dog => {
                // Création du <li>
                const newLi = document.createElement('li');
                newLi.style.display = "flex";
                newLi.style.alignItems = "center";
                newLi.style.gap = "10px";  // espace entre image et nom

                // Création de l'image
                const dogImage = document.createElement('img');
                dogImage.src = dog.image;
                dogImage.alt = "Photo du chien";
                dogImage.width = 100;

                // Création du name
                const dogName = document.createElement('span');
                dogName.textContent = dog.name;

                // Ajout dans le <li>
               newLi.append(dogImage, dogName)

            // Ajout dans la list:
            dogList.append(newLi)
        });

    });
} // fin fonction
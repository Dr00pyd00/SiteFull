

document.addEventListener('DOMContentLoaded', () => {


// les balises a remplir:
    const movieTitle = document.getElementById('movie_title');
    const moviePlot = document.getElementById('movie_plot');
    const movieActorsHeader = document.getElementById('casting');
    const movieActors = document.getElementById('actors');
    const movieBoxHeader = document.getElementById('box_office_header');
    const movieBox = document.getElementById('box_office');
    const msg = document.getElementById('msg');
    
    

// trucs pour form :
    const movieForm = document.getElementById('movie_form');
    const textInput = document.getElementById('movie_text');


// recuperer les datas du front si submit:

    movieForm.addEventListener('submit', (e)=> {
        e.preventDefault();
        console.log('buton submit pressed!');


        // check si le champ est vide :
        if (textInput.value === '') {
            console.log('champs vide ');
            msg.textContent = 'You have no enter a title ! Try again!';
        }else{
            console.log('champ rempli!');
            // mettre les fonctions pour continuer 
            askBackEnd();
        }
    });

    // appel backend:
    function askBackEnd() {
        console.log('fetch lancé!')
        fetch(`/movies/api_request/?movie_title=${encodeURIComponent(textInput.value)}`)
        .then(response => response.json())
        .then( data => {
            if (data.error){
                msg.textContent = data.error;
            } else{
            console.log('data trouvé!')
            fillBalise(data); // remplissage
            console.log(data)
            }
        });
    };

    // remplie les balsies avec la data:
    function fillBalise(data) {

        movieTitle.textContent = data.Title;
        moviePlot.textContent = data.Plot;
        console.log(data.Plot)
        // acteurs , strip et foreach pour les spearer:
        movieActors.innerHTML = '';
        if (data.Actors === 'N/A') {
            const new_li = document.createElement('li');
            movieActorsHeader.textContent = 'Casting';
            new_li.textContent = 'No data sorry !';
            movieActors.append(new_li);
        }else{
            movieActorsHeader.textContent = 'Casting';
            data.Actors.split(', ').forEach( (actor)=> {
            const new_li = document.createElement('li');
            new_li.textContent = actor;
            movieActors.append(new_li);
             });
        }
        // box office on gere si il existe ou pas :
        if (data.BoxOffice === 'N/A') {
            movieBoxHeader.textContent = 'Box Office:';
            movieBox.textContent = 'No data for now !';
        }else{
            movieBoxHeader.textContent = 'Box Office:';
            movieBox.textContent = `${data.BoxOffice.slice(1)} Us dollars.`
        }
    };

























}); //endfull
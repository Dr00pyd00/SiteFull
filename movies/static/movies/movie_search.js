
document.addEventListener('DOMContentLoaded', ()=> {

    // check si js marche:
    console.log('Hello');

    // variables:
    const formMovie = document.getElementById('movie_form');
    const textInput = document.getElementById('textInput');
    const msg = document.getElementById('msg');
    const movieTitle = document.getElementById('title');
    const moviePlot = document.getElementById('plot');
    const movieActors = document.getElementById('actors');
    const movieActorsHeader = document.getElementById('actor_header');
    const movieBoxHeader = document.getElementById('box_header');
    let movieBoxValue = document.getElementById('box_value');

    // check le submit:
    formMovie.addEventListener('submit', (e) =>{
        // empeche le reaload:
        e.preventDefault();
        searchMovie(textInput.value);
    }); 




//======== FONCTIONS ==========//

function searchMovie (user_query) {

    fetch(`https://www.omdbapi.com/?t=${user_query}&apikey=824c66f0`)
    .then(response => response.json())
    .then(data =>{

        // infos :
        const dataTitle = data.Title;

        const dataActors = data.Actors.split(', '); // je rajoute split car c'esdt un string et j'ai besoin de separer chaque acteur.
        const dataPlot = data.Plot;
        let dataBox = data.BoxOffice;
        console.log(`box off =  ${dataBox}` )
        // je gere si y'a pas de value au box office:
        if (dataBox === 'N/A'){
            dataBox = ' This data is not avaible !'
        };

        movieTitle.textContent = dataTitle;
        moviePlot.textContent = dataPlot;

        // titre des parties :
        movieActorsHeader.textContent = 'Casting:';
        movieBoxHeader.textContent = 'Box Office:';
      // value du box office:
      if (dataBox === 'N/A') {
            movieBoxValue.textContent = 'This data is not avaible ! ';
      } else {
            movieBoxValue.textContent = `${dataBox.slice(1)} US Dollars.`;
      };
        
        // boucle pour les acteurs: ( actors est une <ul> )  je vide a chaque submit:
        movieActors.innerHTML = '';
        dataActors.forEach((actor)=>{
            const li = document.createElement('li');
            li.textContent = actor;
            movieActors.append(li);
        });
        

    });

};


}); // end tout
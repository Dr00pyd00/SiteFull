

document.addEventListener('DOMContentLoaded', function() {

        // je setup mes inputs avec les rates dans l'api:
        fetch('https://api.exchangerate-api.com/v4/latest/USD')
        .then(response => response.json())
        .then(data =>  {
            Object.entries(data.rates).forEach( function([monnaie, taux]) {
                
                const fillOption = document.createElement('option');
                fillOption.textContent = `${monnaie}`;
                fillOption.value = monnaie;

                // j'ajoute les 2 selecteurs:
                document.querySelector('#monnaie-entrante').append(fillOption.cloneNode(true));
                document.querySelector('#monnaie-sortante').append(fillOption.cloneNode(true));
            });
        });



        document.querySelector('#convertir').onclick = function() {
          
            // je recupere les valeurs des selecteurs et de l'input:
            const monnaieBase = document.querySelector('#monnaie-entrante').value;
            const monnaieVoulu = document.querySelector('#monnaie-sortante').value;
            const somme = parseFloat(document.querySelector('#somme').value);

            // je dois fetch a nouveau avec la monnaie de base decidé :
            fetch(`https://api.exchangerate-api.com/v4/latest/${monnaieBase}`)
            .then(response => response.json())
            .then(data => {
                // je vais chercher le taux correspondant :
                const taux = data.rates[monnaieVoulu];
                // je fais le calcul:
                const resultat = somme * taux;

                // je vais remplir la div pour display la reponse:
                document.querySelector('#result').innerHTML = `${somme} ${monnaieBase} donne ${resultat.toFixed(2)} ${monnaieVoulu}`


            });            

        };
        


});
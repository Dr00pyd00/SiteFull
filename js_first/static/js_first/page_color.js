
// Choix de la couleur du titre:

document.addEventListener('DOMContentLoaded', function () {

    document.querySelectorAll('button').forEach( function(button) {

        button.onclick = function () {

            document.querySelector('#title').style.color = button.dataset.color;
        }

    })

});


// envoie d'une alert avec ton nom:
 
document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#sub-nom').onclick = function() {
        const name = document.querySelector('#name').value;
        if (name ==='') {
            alert('Tu n\as pas donné ton nom !')
        } else {
            alert(`Salut à toi ${name} !`)
        }
    }
});


    // ecrit la couleur que tu veux pour le titre:

    document.addEventListener('DOMContentLoaded', function() {
        console.log('JS chargé ✅');
        document.querySelector('#set-color').onclick = function() {
            const myColor = document.querySelector('#color-chose').value;
            if (myColor ==='') {
                document.querySelector('#message').innerHTML = 'Tu n\'as pas selectioné de couleur!'
            } else {
                document.querySelector('#write-color').style.color = myColor;
                document.querySelector('#message').innerHTML = '';
            }
        }

    });


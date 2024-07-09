/*Ingreso automatico de libros*/
/*ver en Index ====> section id="catalogo2" */

document.addEventListener('DOMContentLoaded', function () {
    const catalogoContainer = document.querySelector('#catalogo2');
    const libros = 
    [
        { titulo: "Al costado de la luna", autor: "Graciela Geller", año: 2006, 
        imagenurl: "./assets/img/catalogo/lib-cat-1.jpeg",         
        },

        { titulo: "Opus Dos", autor: "Angélica Gorodischer", año: 1967, 
        imagenurl: "./assets/img/catalogo/lib-cat-2.jpg",         
        },

        { titulo: "El Psicoanalista", autor: "John Katzenbach", año: 2002,  
        imagenurl: "./assets/img/catalogo/lib-cat-3.png",        
        },

        { titulo: "Metro 2033", autor: "Dmitry Gluhovsky", año: 2002, 
        imagenurl:"./assets/img/catalogo/lib-cat-4.png",        
        },

        { titulo: "Yo Matias", autor: "Sendra", año: 2006, 
        imagenurl: "./assets/img/catalogo/lib-cat-5.png",          
        },

        { titulo: "La alegria de cocinar", autor: "El Arguiñano", año: 1954, 
        imagenurl: "./assets/img/catalogo/lib-cat-6.png",        
        },
        ,
    ];
   
    libros.forEach(libro => {
        const card = document.createElement('div');
        card.className = 'card-container';
        card.innerHTML = `
            <div class="card-title">
                <p>${libro.titulo}</p>
            </div>
            
            <div class="card-body">
                <img src="${libro.imagenurl}">               
            </div>
            
            <div class="card-foot"> 
                <p>${libro.autor} - ${libro.año}</p>
            </div>
        `;
        document.querySelector('.cards-catalogo').appendChild(card); // Aquí se modifica
    });
});


/*El html ingresado - correspondiente a las card de libros*/
/*

<div class="card-container">
    <div class="card-title">
        <p>${libro.titulo}</p>
    </div>

    <div class="card-body">
        <img src="${libro.imagenurl}">
            <p class="card-text">Descripción breve del libro</p>
    </div>

    <div class="card-foot">
        <p>${libro.autor} - ${libro.año}</p>
    </div>
</div>

*/
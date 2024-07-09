/*Ingreso automatico del carousel*/
/*ver en Index ====> section id="carousel" */


document.addEventListener('DOMContentLoaded', function () {

    /*Variable contenedora de todo el html editado*/
    var carouselCliente =
        `
    <div id="carouselExampleCaptions" class="carousel slide">
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0"
            class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"
            aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"
            aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="./assets/img/carrousel/1-fernando-sendra.jpg" class="d-block w-100"
                alt="FernandoSendra">
            <div class="carousel-caption d-none d-md-block">
                <h5>Fernando Sendra</h5>
                <p>Escritor, humorista gráfico, dibujante, guionista y historietista argentino. Su
                    personaje más conocido es Matías, el principal de la tira Yo, Matías.</p>
            </div>
        </div>
        <div class="carousel-item">
            <img src="./assets/img/carrousel/2-dmitry-glukhovsky.jpg" class="d-block w-100"
                alt="DmitriGlukhovsky">
            <div class="carousel-caption d-none d-md-block">
                <h5>Dmitri Glukhovsky</h5>
                <p>Escritor y periodista ruso conocido por el éxito de la novela de ciencia ficción y
                    fantasía post-apocalíptica Metro 2033 y sus secuelas. El éxito de su primera novela
                    ha dado origen a una franquicia conocida como Metro (Метро) popular en diversos
                    géneros como novelas o videojuegos y en muchos países.</p>
            </div>
        </div>
        <div class="carousel-item">
            <img src="./assets/img/carrousel/3-angelica-gorodischer.jpg" class="d-block w-100"
                alt="Angélica Gorodischer">
            <div class="carousel-caption d-none d-md-block">
                <h5>Angélica Gorodischer</h5>
                <p>Escritora argentina, ha publicado su primer obra "Opus Dos" con nuestra editorial.
                    Sus narraciones integran antologías de distintos países y publica en diarios y
                    revistas de distintas latitudes. </p>
            </div>
        </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions"
        data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions"
        data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
    </div>
    `

    document.getElementById("clientes-carousel").innerHTML = carouselCliente;
});
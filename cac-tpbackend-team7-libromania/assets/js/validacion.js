//Validación del formulario de registro

function validarFormulario(event) {
    event.preventDefault();
    var nombre = document.getElementById('nombreUsuario').value;
    var apellido = document.getElementById('apellidoUsuario').value;
    var email = document.getElementById('emailUsuario').value;
    var contraseña = document.getElementById('contraseñaUsuario').value;
    var tipoDocumento = document.getElementById('tipoDeDocDelUsuario').value;
    var numeroDocumento = document.getElementById('identificacionUsuario').value;
    var terminos = document.getElementById('terminos').checked;

    if (nombre === '' || apellido === '' || email === '' || contraseña === '' || tipoDocumento === '' || numeroDocumento === '' || !terminos) {
        alert('Por favor, complete todos los campos y acepte los términos y condiciones.');
    } else {
        alert('Formulario enviado correctamente.');
        window.location.href = '../pages/bienvenida.html'; //Nos dirige a la pagina de bienvenida, en desarrollo
    }
}

window.onload = function() {
    document.querySelector('form').addEventListener('submit', validarFormulario);
}

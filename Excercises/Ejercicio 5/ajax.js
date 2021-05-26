
function ajax_Form(){
    // Tomamos los datos ingresados en el formulario
    let nombre = document.getElementById('nombre-medico').value;
    let experiencia = document.getElementById('experiencia-medico').value;
    let especialidad = document.getElementById('especialidad-medico').value;
    let email = document.getElementById('email-medico').value;
    let celular = document.getElementById('celular-medico').value;

    console.log('Formulario enviado');
    let data = new FormData();
    data.append('nombre-medico', nombre);
    data.append('experiencia-medico', experiencia);
    data.append('especialidad-medico', especialidad);
    data.append('email-medico', email);
    data.append('celular-medico', celular);
    data.append('file', document.getElementById('file').files[0]);

    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'cgi-bin/save_doctor.py', true);
    xhr.timeout = 300;
    xhr.onload = function (data) {
        alert('Enviado correctamente!');
        console.warn(data.currentTarget.responseText);
    };
    xhr.send(data);
    return false;
}

function ajax_List(){
    let data = new FormData();
    let xhr  = new XMLHttpRequest();
    xhr.open('POST', 'list.py');
    xhr.timeout = 300;
    console.log('read')

    xhr.onload = function(data){
        let text = data.currentTarget.responseText;
        console.log(text)
        document.getElementById("data").innerHTML = text
    };
    xhr.onerror = function(){
        showError('Fatal error');
    }
    xhr.send(data);
}
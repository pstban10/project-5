
let ejerciciosAgregados = [];

function agregarEjercicio(nombreEjercicio) {
    ejerciciosAgregados.push({ nombre: nombreEjercicio, repeticiones: 0, sets: 0 });
    actualizarTablaEjerciciosAgregados();
}

function actualizarTablaEjerciciosAgregados() {
    const tbody = document.getElementById("ejercicios-agregados");
    // Limpiar el contenido actual
    tbody.innerHTML = "";
    // Agregar filas para cada ejercicio en la lista
    ejerciciosAgregados.forEach(ejercicio => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
                <td>${ejercicio.nombre}</td>
                <td><input type="number" value="${ejercicio.repeticiones}" onchange="actualizarRepeticiones('${ejercicio.nombre}', this.value)"></td>
                <td><input type="number" value="${ejercicio.sets}" onchange="actualizarSets('${ejercicio.nombre}', this.value)"></td>
                <td><button class="btn btn-danger me-md-2" type="button" onclick="eliminarEjercicio('${ejercicio.nombre}')">Eliminar</button></td>
            `;
        tbody.appendChild(fila);
    });
}

function actualizarRepeticiones(nombreEjercicio, valor) {
    const ejercicio = ejerciciosAgregados.find(ejercicio => ejercicio.nombre === nombreEjercicio);
    if (ejercicio) {
        ejercicio.repeticiones = parseInt(valor);
    }
}

function actualizarSets(nombreEjercicio, valor) {
    const ejercicio = ejerciciosAgregados.find(ejercicio => ejercicio.nombre === nombreEjercicio);
    if (ejercicio) {
        ejercicio.sets = parseInt(valor);
    }
}


function eliminarEjercicio(nombreEjercicio) {
    var index = ejerciciosAgregados.findIndex(ejercicio => ejercicio.nombre === nombreEjercicio);
    if (index !== -1) {
        ejerciciosAgregados.splice(index, 1);
        actualizarTablaEjerciciosAgregados();
    }
}
// hasta aqui tengo una lista con los ejercicios que quiero agregar a la DB


function guardarCambios(routine) {
    const form = document.getElementById("form-rutina-exercise");

    // Crear un array de objetos con los valores de ejerciciosAgregados
    const ejerciciosAgregadosData = ejerciciosAgregados.map(ejercicio => ({
        routine_id: routine,
        exercise: ejercicio.nombre,
        repetitions: ejercicio.repeticiones,
        sets: ejercicio.sets
    }));

    const jsonEjerciciosAgregados = JSON.stringify(ejerciciosAgregadosData);

    return jsonEjerciciosAgregados;
}



function guardarRutina() {

}

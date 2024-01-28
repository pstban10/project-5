const listarHorarios = async (idLugar, idDay) => {
    const data = await seleccionarFecha()

    try {
        const response = await fetch(`./horarios/${idLugar}/${idDay}`)
        const data = await response.json()
        if (data.Mensaje == "Éxito") {
            let opciones = ``;
            data.horarios.forEach((horario) => {
                opciones += `<option value='${horario.id}'>${horario.hour}</option>`;
            });
            hours.innerHTML = opciones
        } else {
            alert('no hay nada bro')
        }
    } catch (error) {
        console.log(`Hay un error al cargar los horarios: ${error}`)
    }
}

const listarLugares = async () => {
    try {
        const response = await fetch('./reservar')
        const data = await response.json()
        if (data.Mensaje == "Éxito") {
            let opciones = ``;
            data.puntos.forEach((punto) => {
                opciones += `<option value='${punto.id}'>${punto.name}</option>`;
            });
            Locations.innerHTML = opciones
        } else {
            alert('no hay nada bro')
        }
    } catch (error) {
        console.log(`Hay un error al cargar los lugares: ${error}`)
    }
}

const cargaInicial = async () => {
    await listarLugares();
    Locations.addEventListener("change", (event) => {
        let dataLugar = event.target.value
        seleccionarFecha()

    })
}

const seleccionarFecha = async () => {

    fecha.addEventListener("change", (event) => {
        let dataFecha = new Date(event.target.value + 'T12:00:00')

        const opcionesFecha = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        const formatoFecha = new Intl.DateTimeFormat('es-ES', opcionesFecha);

        const fechaFormateada = formatoFecha.format(dataFecha);

        console.log(`El día ${fechaFormateada} es tu clase de prueba en ${dataLugar}`);
    });
    listarHorarios(dataLugar, fechaFormateada.day)
}
window.addEventListener("load", async () => {
    await cargaInicial();
})
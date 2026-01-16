/* selección de elementos del DOM */

const form = document.getElementById("formCita");
const nombre = document.getElementById("nombre");
const edad = document.getElementById("edad");
const email = document.getElementById("email");
const especialidad = document.getElementById("especialidad");
const turno = document.getElementsByName("turno");
const terminos = document.getElementById("terminos");
const listaCitas = document.getElementById("listaCitas");

const errorNombre = document.getElementById("errorNombre");
const errorEdad = document.getElementById("errorEdad");
const errorEmail = document.getElementById("errorEmail");
const errorEspecialidad = document.getElementById("errorEspecialidad");
const errorTurno = document.getElementById("errorTurno");
const errorTerminos = document.getElementById("errorTerminos");

/* funciones reutilizables */

function mostrarError(campo, span, mensaje) {
  span.textContent = mensaje;

  if (campo) {
    campo.classList.add("invalid");
  }
}

function limpiarError(campo, span) {
  span.textContent = "";

  if (campo) {
    campo.classList.remove("invalid");
  }
}

function crearElemento(tag, texto) {
  const el = document.createElement(tag);
  el.textContent = texto;
  return el;
}

/* validaciones */
function validarFormulario() {
  let valido = true;

  // Nombre
  if (nombre.value.length < 3) {
    mostrarError(nombre, errorNombre, "Mínimo 3 caracteres");
    valido = false;
  } else {
    limpiarError(nombre, errorNombre);
  }

  // Edad (un minimo de 18 años)
  if (edad.value < 18 || edad.value > 120) {
    mostrarError(edad, errorEdad, "Debes tener al menos 18 años");
    valido = false;
  } else {
    limpiarError(edad, errorEdad);
  }

  // Email
  if (!email.value.includes("@")) {
    mostrarError(email, errorEmail, "Email inválido");
    valido = false;
  } else {
    limpiarError(email, errorEmail);
  }

  // Select
  if (especialidad.value === "") {
    mostrarError(especialidad, errorEspecialidad, "Selecciona especialidad");
    valido = false;
  } else {
    limpiarError(especialidad, errorEspecialidad);
  }

  // Radio
  let turnoMarcado = false;

  for (let r of turno) {
    if (r.checked) {
      turnoMarcado = true;
    }
  }

  if (!turnoMarcado) {
    errorTurno.textContent = "Selecciona un turno";
    valido = false;
  } else {
    errorTurno.textContent = "";
  }

  // Checkbox
  if (!terminos.checked) {
    errorTerminos.textContent = "Debes aceptar los términos y condiciones";
    valido = false;
  } else {
    errorTerminos.textContent = "";
  }

  return valido;
}

/* EVENTOS  (INPUT Y CHANGE)*/
// A continuacion validamos con addEventListener nombre, edad, email,
//especialidad, turno y términos)

// input y change para quitar mensaje de error

nombre.addEventListener("input", function () {
  validarFormulario();
});

edad.addEventListener("input", function () {
    validarFormulario();
});

email.addEventListener("input", function () {
    validarFormulario();
});

for (let r of turno) {
    r.addEventListener("change", function () {
        validarFormulario();
    });
}

terminos.addEventListener("change", function () {
    validarFormulario();
});

especialidad.addEventListener("change", function () {
    validarFormulario();

    if (especialidad.value !== "") {
        especialidad.classList.add("seleccionado");
    } else {
        especialidad.classList.remove("seleccionado");
    }
});

/* EVENTOS  (SUBMIT Y CLICK)*/

// submit
form.addEventListener("submit", function (e) {
  e.preventDefault();

  if (validarFormulario()) {
    const cita = document.createElement("div");
    cita.className = "cita";
    cita.dataset.nombre = nombre.value; // dataset

    cita.appendChild(crearElemento("p", "Nombre: " + nombre.value));
    cita.appendChild(crearElemento("p", "Especialidad: " + especialidad.value));

    const btnEliminar = crearElemento("button", "Eliminar");

    btnEliminar.addEventListener("click", function () {
      btnEliminar.closest(".cita").remove(); // closest + remove
    });

    cita.appendChild(btnEliminar);
    listaCitas.appendChild(cita);

    form.reset();
  }
});

// BOM
document.getElementById("guardarDatos").addEventListener("click", function () {
  localStorage.setItem("nombre", nombre.value);
});

document.getElementById("restaurarDatos").addEventListener("click", function () {
  nombre.value = localStorage.getItem("nombre") || "";
});

document.getElementById("recargar").addEventListener("click", function () {
  location.reload();
});

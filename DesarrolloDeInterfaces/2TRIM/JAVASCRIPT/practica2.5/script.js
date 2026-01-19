/* selección de elementos del DOM */
const form = document.getElementById("formCita");
const nombre = document.getElementById("nombre");
const edad = document.getElementById("edad");
const email = document.getElementById("email");
const especialidad = document.getElementById("especialidad");
const turno = document.getElementsByName("turno");
const terminos = document.getElementById("terminos");
const motivo = document.getElementById("motivo");
const listaCitas = document.getElementById("listaCitas");

const errorNombre = document.getElementById("errorNombre");
const errorEdad = document.getElementById("errorEdad");
const errorEmail = document.getElementById("errorEmail");
const errorEspecialidad = document.getElementById("errorEspecialidad");
const errorTurno = document.getElementById("errorTurno");
const errorTerminos = document.getElementById("errorTerminos");

const errorLimite = document.getElementById("errorLimite");

/* especialidad “otra” */
const wrapOtra = document.getElementById("wrapOtra");
const otraEspecialidad = document.getElementById("otraEspecialidad");
const errorOtraEspecialidad = document.getElementById("errorOtraEspecialidad");

/* funciones reutilizables */
function mostrarError(campo, span, mensaje) {
  span.textContent = mensaje;
  if (campo) campo.classList.add("invalid");
}

function limpiarError(campo, span) {
  span.textContent = "";
  if (campo) campo.classList.remove("invalid");
}

function crearElemento(tag, texto) {
  const el = document.createElement(tag);
  el.textContent = texto;
  return el;
}

/* sacar el turno marcado */
function obtenerTurno() {
  for (let r of turno) {
    if (r.checked) return r.value;
  }
  return "";
}

/* sacar especialidad final (select u “otra”) */
function obtenerEspecialidadFinal() {
  if (especialidad.value === "Otra") {
    return otraEspecialidad.value.trim();
  }
  return especialidad.value;
}

/* validaciones */
function validarFormulario() {
  let valido = true;

  // limpiar mensaje límite (para que no se quede fijo)
  errorLimite.textContent = "";

  // Nombre
  if (nombre.value.trim().length < 3) {
    mostrarError(nombre, errorNombre, "Mínimo 3 caracteres");
    valido = false;
  } else {
    limpiarError(nombre, errorNombre);
  }

  // Edad
  if (Number(edad.value) < 18 || Number(edad.value) > 120) {
    mostrarError(edad, errorEdad, "Debes tener al menos 18 años");
    valido = false;
  } else {
    limpiarError(edad, errorEdad);
  }

  // Email (con mensajes separados)
  const e = email.value.trim();

  if (e === "") {
    mostrarError(email, errorEmail, "Falta el correo");
    valido = false;
  } else if (!e.includes("@")) {
    mostrarError(email, errorEmail, "Falta el @");
    valido = false;
  } else if (!e.includes(".")) {
    mostrarError(email, errorEmail, "Falta el punto (.)");
    valido = false;
  } else {
    limpiarError(email, errorEmail);
  }

  // Especialidad (select obligatorio)
  if (especialidad.value === "") {
    mostrarError(especialidad, errorEspecialidad, "Selecciona especialidad");
    valido = false;
  } else {
    limpiarError(especialidad, errorEspecialidad);
  }

  // Si es “Otra”, también obligo a escribir algo
  if (especialidad.value === "Otra") {
    if (otraEspecialidad.value.trim().length < 3) {
      mostrarError(otraEspecialidad, errorOtraEspecialidad, "Escribe la especialidad (mín. 3 letras)");
      valido = false;
    } else {
      limpiarError(otraEspecialidad, errorOtraEspecialidad);
    }
  } else {
    // si no es “Otra”, limpio por si quedaba algo
    limpiarError(otraEspecialidad, errorOtraEspecialidad);
  }

  // Turno (radio)
  const turnoElegido = obtenerTurno();
  if (turnoElegido === "") {
    errorTurno.textContent = "Selecciona un turno";
    valido = false;
  } else {
    errorTurno.textContent = "";
  }

  // Términos (checkbox)
  if (!terminos.checked) {
    errorTerminos.textContent = "Debes aceptar los términos y condiciones";
    valido = false;
  } else {
    errorTerminos.textContent = "";
  }

  return valido;
}

/* eventos input/change para validar */
nombre.addEventListener("input", validarFormulario);
edad.addEventListener("input", validarFormulario);
email.addEventListener("input", validarFormulario);

for (let r of turno) {
  r.addEventListener("change", validarFormulario);
}

terminos.addEventListener("change", validarFormulario);

/* select especialidad: mostrar el input “otra” */
especialidad.addEventListener("change", function () {
  validarFormulario();

  if (especialidad.value === "Otra") {
    wrapOtra.classList.remove("oculto");
  } else {
    wrapOtra.classList.add("oculto");
    otraEspecialidad.value = "";
  }

  if (especialidad.value !== "") {
    especialidad.classList.add("seleccionado");
  } else {
    especialidad.classList.remove("seleccionado");
  }
});

otraEspecialidad.addEventListener("input", validarFormulario);

/* submit */
form.addEventListener("submit", function (e) {
  e.preventDefault();

  // límite: solo 2 citas
  if (listaCitas.children.length >= 2) {
    errorLimite.textContent = "Ya no se puede crear más citas. Elimina una cita para poder añadir otra.";
    return;
  }

  if (validarFormulario()) {
    const cita = document.createElement("div");
    cita.className = "cita";

    const turnoFinal = obtenerTurno();
    const especFinal = obtenerEspecialidadFinal();

    // guardo datos por si luego quiero usarlos
    cita.dataset.turno = turnoFinal;
    cita.dataset.especialidad = especFinal;

    // resumen de la cita (más completo)
    cita.appendChild(crearElemento("p", "Nombre: " + nombre.value));
    cita.appendChild(crearElemento("p", "Email: " + email.value));
    cita.appendChild(crearElemento("p", "Especialidad: " + especFinal));
    cita.appendChild(crearElemento("p", "Turno: " + turnoFinal));

    const btnEliminar = crearElemento("button", "Eliminar");

    btnEliminar.addEventListener("click", function () {
      btnEliminar.closest(".cita").remove();
      errorLimite.textContent = ""; // si borran, quito el mensaje del límite
    });

    cita.appendChild(btnEliminar);
    listaCitas.appendChild(cita);

    form.reset();
    especialidad.classList.remove("seleccionado");
    wrapOtra.classList.add("oculto");
  }
});

/* BOM (click) */
document.getElementById("guardarDatos").addEventListener("click", function () {
  localStorage.setItem("nombre", nombre.value);
  localStorage.setItem("edad", edad.value);
  localStorage.setItem("email", email.value);
  localStorage.setItem("especialidad", especialidad.value);
  localStorage.setItem("otraEspecialidad", otraEspecialidad.value);
  localStorage.setItem("motivo", motivo.value);

  // guardo turno
  localStorage.setItem("turno", obtenerTurno());
});

document.getElementById("restaurarDatos").addEventListener("click", function () {
  nombre.value = localStorage.getItem("nombre") || "";
  edad.value = localStorage.getItem("edad") || "";
  email.value = localStorage.getItem("email") || "";
  especialidad.value = localStorage.getItem("especialidad") || "";
  otraEspecialidad.value = localStorage.getItem("otraEspecialidad") || "";
  motivo.value = localStorage.getItem("motivo") || "";

  // restaurar turno
  const t = localStorage.getItem("turno") || "";
  for (let r of turno) {
    r.checked = (r.value === t);
  }

  // si especialidad es “Otra”, muestro el input
  if (especialidad.value === "Otra") {
    wrapOtra.classList.remove("oculto");
  } else {
    wrapOtra.classList.add("oculto");
  }

  // revalidar
  validarFormulario();
});

document.getElementById("recargar").addEventListener("click", function () {
  location.reload();
});

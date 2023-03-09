// Funciones para formato moneda y porcentaje

const inputs_moneda = document.querySelectorAll(".input-moneda");

inputs_moneda.forEach((mi_input) => {
  mi_input.addEventListener('change', updateValue);

  function updateValue(e) {
    const f = new Intl.NumberFormat("es-cl", {
      currency: "CLP",
      style: "currency",
    })
    mi_input.setAttribute("type", "text");
    mi_input.value = f.format(e.target.value);
    mi_input.blur();
  }

  mi_input.addEventListener('focus', () => {
    mi_input.value = ''
    mi_input.setAttribute("type", "number");
  })
})

const inputs_porcentaje = document.querySelectorAll(".input-porcentaje");

inputs_porcentaje.forEach((mi_input) => {
  mi_input.addEventListener('change', updateValue);

  function updateValue(e) {
    const f = new Intl.NumberFormat("es-cl", {
      style: "percent",
      minimumFractionDigits: 2,
    })
    const valor = parseFloat(e.target.value);
    mi_input.setAttribute("type", "text");
    mi_input.value = f.format(valor / 100);
    mi_input.blur();
  }

  mi_input.addEventListener('focus', () => {
    mi_input.value = "";
    mi_input.setAttribute("type", "number");
  })
})

function setRadioPrecisionAttributes() {
  const radio_precision = document.querySelector("#div_id_precision > div");
  const t_mensaje = "Precisión del cálculo opcional"
  const mensaje = 'En plazos extensos afecta al tiempo de respuesta. Una mayor precisión, entrega un resultado más ajustado a lo buscado. (Se recomienda usa "Alta" y "Muy alta", solamente para afinar el presupuesto final)'
    radio_precision.setAttribute("data-bs-toggle", "popover")
    radio_precision.setAttribute("data-bs-trigger", "hover")
    radio_precision.setAttribute("data-bs-original-title", t_mensaje)
    radio_precision.setAttribute("data-bs-content", mensaje)
  }
setRadioPrecisionAttributes();


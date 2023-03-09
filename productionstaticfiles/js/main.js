var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})
var popover = new bootstrap.Popover(document.querySelector('.popover-dismiss'), {
    trigger: 'focus'
  })


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
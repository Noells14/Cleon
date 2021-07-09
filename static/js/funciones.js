const vivienda_open = document.getElementById('vivienda_open');
const vivienda_modal = document.getElementById('vivienda_modal');
const vivienda_close = document.getElementById('vivienda_close');
const diseño_open = document.getElementById('diseño_open');
const diseño_modal = document.getElementById('diseño_modal');
const diseño_close = document.getElementById('diseño_close');
const oficina_open = document.getElementById('oficina_open');
const oficina_modal = document.getElementById('oficina_modal');
const oficina_close = document.getElementById('oficina_close');

vivienda_open.addEventListener('click', () => {
    vivienda_modal.classList.add('show');
});

vivienda_close.addEventListener('click', () => {
    vivienda_modal.classList.remove('show');
});

diseño_open.addEventListener('click', () => {
    diseño_modal.classList.add('show');
});

diseño_close.addEventListener('click', () => {
    diseño_modal.classList.remove('show');
});

oficina_open.addEventListener('click', () => {
    oficina_modal.classList.add('show');
});

oficina_close.addEventListener('click', () => {
    oficina_modal.classList.remove('show');
});
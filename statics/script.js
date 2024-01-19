const select = document.getElementById('tabla');
const datosDiv = document.getElementById('datos');
const loading = document.getElementById('loading');

select.addEventListener('change', () => {

    let tabla = select.value;
    select.disabled = true;
    loading.style.display = 'flex';

    fetch(`http://localhost:5000/datos?tabla=${tabla}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not OK');
            }
            return response.text();
        })
        .then(data => {
            select.disabled = false;
            loading.style.display = 'none';
            datosDiv.innerHTML = data;
        })
        .catch(error => {
            select.disabled = false;
            loading.style.display = 'none';
            console.error('There has been a problem with your fetch operation:', error);
        });
});
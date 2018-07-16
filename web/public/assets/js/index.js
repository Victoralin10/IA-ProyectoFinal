$(document).ready(() => {
    function updateEvents() {
        $.get('/api/events', res => {
            if (res.success) {

                $('#table-body-id>tr').remove();
                let tBody = $('#table-body-id');

                res.data.forEach(ev => {
                    console.log(ev.timestamp);

                    let fecha = Date.parse(ev.timestamp);
                    fecha = new Date(fecha);

                    tBody.append(`<tr>
                                  <th scope="row">${ev.id}</th>
                                  <td>${ev.station}</td>
                                  <td>${ev.description}</td>
                                  <td>${fecha}</td></tr>`);
                });
            }
        });
    }

    setInterval(updateEvents, 10000);
    updateEvents();
});

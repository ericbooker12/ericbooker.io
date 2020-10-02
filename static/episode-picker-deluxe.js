$('.form').submit(event => {
    event.preventDefault();
    let showName = $('#show').val();

    // console.log(showName);


    $.ajax({
        type: 'GET',
        url: "/get-show-data",
        data: { "show": showName },
        success: function(response) {
            console.log(response)
                // let address = response[1]
                // let table_str = '';
                // for (address_component in address) {
                //     table_str += `
                // <tr>
                //   <td> ${address[address_component]} </td>
                //   <td> ${address_component} </td>
                // </tr>`
                // }

            // $('#address-results tbody').html(table_str);
            // $('#address-results').css('display', '');
        },
        error: function(response) {
            let err_msg = `
          <div id="err_msg" class="alert alert-danger">
            Error. Some Error.
          </div>  
        `

        }
    })
})
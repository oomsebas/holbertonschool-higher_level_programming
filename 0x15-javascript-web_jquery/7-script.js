$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, state) => {
    if (state == 'success') {
      $('#character').html(data.name);
    }
   });
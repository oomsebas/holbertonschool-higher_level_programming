$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    for (let i in data.results) {
        $('#list_movies').append('<li>' + data.results[i].title + '</li>');
    }
});
#!/usr/bin/node
// request starwars movie according to an id
const request = require('request');
const args = process.argv.slice(2);

request('https://swapi-api.hbtn.io/api/films/' + args[0],
  function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      console.log(JSON.parse(body).title);
    }
  });

#!/usr/bin/node
// Write a script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const args = process.argv.slice(2);
request(args[0], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const res = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < res.length; i++) {
      const characters = res[i].characters;
      for (const char in characters) {
        if (characters[char].indexOf('18') >= 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

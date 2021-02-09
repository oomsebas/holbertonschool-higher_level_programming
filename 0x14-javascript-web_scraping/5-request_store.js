#!/usr/bin/node
// request a web page

const fs = require('fs');
const request = require('request');
const args = process.argv.slice(2);

request(args[0],
  function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      fs.writeFile(args[1], body, 'utf-8', (err) => {
        if (err) throw err;
      });
    }
  });

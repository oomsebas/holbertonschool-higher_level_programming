#!/usr/bin/node
// make a GET request

const request = require('request');
const args = process.argv.slice(2);

request
  .get(args[0])
  .on('response', function (response) {
    console.log('code: ' + response.statusCode); // 200
  });

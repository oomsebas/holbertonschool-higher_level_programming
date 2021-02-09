#!/usr/bin/node
// request to an API an print the tasks completed

const request = require('request');
const args = process.argv.slice(2);

request(args[0],
  function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      const res = JSON.parse(body);
      const dict = {};
      for (const item in res) {
        if (res[item].completed === true) {
          if (dict[res[item].userId] === undefined) {
            dict[res[item].userId] = 1;
          } else {
            dict[res[item].userId] += 1;
          }
        }
      }
      console.log(dict);
    }
  });

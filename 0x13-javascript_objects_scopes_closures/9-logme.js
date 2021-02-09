#!/usr/bin/node
// Write a function that prints the number of arguments already printed and
// the new argument value. (see example below)
let count = 0;

exports.logMe = function (item) {
  console.log('%d: %s', count, item);
  count += 1;
};

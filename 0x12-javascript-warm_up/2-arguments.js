#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments

const myArgs = process.argv.slice(2);
const len = myArgs.length;
if (len === 0) {
  console.log('No argument');
} else {
  len === 1 ? console.log('Argument found') : console.log('Arguments found');
}

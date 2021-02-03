#!/usr/bin/node
// Write a script that prints a square

const args = process.argv.slice(2);
const side = Number(args[0]);
let line = '';
if (!(side)) {
  console.log('Missing size');
} else if (side > 0) {
  for (let j = 0; j < side; j++) {
    for (let i = 0; i < side; i++) {
      line += 'X';
    }
    console.log(line);
    line = '';
  }
}

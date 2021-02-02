#!/usr/bin/node
// Write a script that prints x times “C is fun”

const args = process.argv.slice(2);
const loop = Number(args[0]);
if (!(loop)) {
  console.log('Missing number of occurrences');
} else if (loop > 0) {
  for (let i = 0; i < loop; i++) {
    console.log('C is fun');
  }
}

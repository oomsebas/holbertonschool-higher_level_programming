#!/usr/bin/node
// Write a script that computes and prints a factorial

const fact = Number(process.argv.slice(2)[0]);
let mult = 1;

if (!fact) {
  console.log('1');
} else {
  for (let i = 1; i <= fact; i++) {
    mult = mult * i;
  }
  console.log(mult);
}

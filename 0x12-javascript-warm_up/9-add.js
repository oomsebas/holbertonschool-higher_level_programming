#!/usr/bin/node
// Write a script that prints the addition of 2 integers

const lst = process.argv.slice(2);
const num1 = Number(lst[0]);
const num2 = Number(lst[1]);

function add (a, b) {
  const res = a + b;
  return (res);
}
const sumPair = add(num1, num2);
console.log(sumPair);

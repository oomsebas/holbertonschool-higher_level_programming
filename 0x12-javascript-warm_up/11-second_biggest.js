#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
let lst = process.argv.slice(2);
if (lst.length === 0 || (lst.length === 1)) {
  console.log(0);
} else {
  lst = lst.map(Number);
  console.log(lst.sort(function (a, b) { return a - b; }));
  const res = Number(lst.sort()[lst.length - 2]);
  console.log(res);
}

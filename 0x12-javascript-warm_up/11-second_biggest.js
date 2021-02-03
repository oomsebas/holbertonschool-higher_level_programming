#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
const lst = process.argv.slice(2);
if (lst.length === 0 || (lst.length === 1)) {
  console.log(0);
} else {
  lst.sort(function (a, b) { return a - b; });
  lst.reverse();
  console.log(lst[1]);
}

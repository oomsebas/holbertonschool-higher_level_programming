#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
const lst = process.argv.slice(2);
if (lst.length === 0 || (lst.length === 1)) {
  console.log(0);
} else {
  const res = lst.sort()[lst.length - 2];
  console.log(res);
}

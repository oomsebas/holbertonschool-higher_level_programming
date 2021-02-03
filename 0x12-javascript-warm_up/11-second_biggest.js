#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
let lst = process.argv.slice(2);
if (lst.length === 0 || (lst.length === 1)) {
  console.log(0);
} else {
  lst = lst.map(Number);
  for (let i = 0; i < lst.length; i++) {
    if (lst[i + 1] < lst[i]) {
      const temp = lst[i + 1];
      lst[i + 1] = lst[i];
      lst[i] = temp;
    }
  }
  console.log(lst[lst.length - 2]);
}

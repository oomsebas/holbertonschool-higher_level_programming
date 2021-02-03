#!/usr/bin/node
// Write a script that computes and prints a factorial

const fact = Number(process.argv.slice(2)[0]);

function factorial (a) {
  const mult = 1;
  const i = 1;
  let res = 0;
  if (!a) {
    console.log('1');
  } else {
    res = acum(mult, i, a);
    console.log(res);
  }
}

function acum (mult, i, a) {
  let res = 0;

  mult *= i;
  i = i + 1;
  if (i > a) {
    return (mult);
  }
  res = acum(mult, i, a);
  return (res);
}

factorial(fact);

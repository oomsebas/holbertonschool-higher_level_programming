#!/usr/bin/node
//Write a script that prints My number: <first argument converted in integer>

const args = process.argv.slice(2);
const number = Number(args);
number ? console.log('My number: ' + args[0]) : console.log('Not a number')

#!/usr/bin/node
// print to the console the first argument passed

const myVar = process.argv.slice(2);
myVar[0] ? console.log(myVar[0]) : console.log('No argument');

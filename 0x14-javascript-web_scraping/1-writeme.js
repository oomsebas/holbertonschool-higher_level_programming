#!/usr/bin/node
// Write a script that writes a string to a file.

const fs = require('fs');
const args = process.argv.slice(2);

fs.writeFile(args[0], args[1], (err) => {
  if (err) throw err;
});

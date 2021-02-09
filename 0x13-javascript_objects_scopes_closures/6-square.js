#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const line = c != null ? c : 'X';
    for (let j = 0; j < this.height; j++) {
      console.log(line.repeat(this.width));
    }
  }
}
module.exports = Square;

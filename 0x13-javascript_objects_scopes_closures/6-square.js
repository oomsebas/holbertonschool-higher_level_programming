#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    const line = c;
    for (let j = 0; j < this.height; j++) {
      console.log(line.repeat(this.width));
    }
  }
}
module.exports = Square;

#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}
module.exports = Square;

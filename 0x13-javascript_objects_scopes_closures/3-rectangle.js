#!/usr/bin/node
// Write a class Rectangle that defines a rectangle:

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const line = 'X';
    for (let j = 0; j < this.height; j++) {
      console.log(line.repeat(this.width));
    }
  }
}
module.exports = Rectangle;

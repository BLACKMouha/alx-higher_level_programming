#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const x = [];
      for (let j = 0; j < this.width; j++) {
        x.push('X');
      }
      console.log(x.join(''));
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};

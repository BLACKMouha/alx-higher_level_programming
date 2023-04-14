#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const s = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(s);
    }
  }

  rotate () {
    const i = this.width;
    this.width = this.height;
    this.height = i;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

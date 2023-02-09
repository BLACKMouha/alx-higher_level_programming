#!/usr/bin/node
const OtherSquare = require('./5-square');

module.exports = class Square extends OtherSquare {
  constructor (size) {
    super(size, size);
  }
 
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        const chars = [];
        for (let j = 0; j < this.width; j++) {
          chars.push(c);
        }
        console.log(chars.join(''));
      }
    } else {
      super.print();
    }
  }
};

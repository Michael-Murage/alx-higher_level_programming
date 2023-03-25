#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log((!c ? 'X' : c).repeat(this.width));
    }
  }
}

module.exports = Square;

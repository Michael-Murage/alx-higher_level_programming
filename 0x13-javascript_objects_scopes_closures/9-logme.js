#!/usr/bin/node
let counterArgs = 0;
exports.logMe = function (item) {
  console.log(`${counterArgs}: ${item}`);
  counterArgs++;
};

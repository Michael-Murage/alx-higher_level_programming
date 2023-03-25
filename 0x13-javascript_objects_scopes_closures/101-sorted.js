#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = Object.entries(dict).reduce((prev, [key, val]) => {
  prev[val] = prev[val] ? [...prev[val], key] : [key];
  return prev;
}, {});

console.log(newDict);

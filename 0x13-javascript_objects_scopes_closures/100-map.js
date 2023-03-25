#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((elem, idx) => elem * idx);

console.log(list);
console.log(newList);

#!/usr/bin/node
const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2], 'utf8', function (err, res) {
  if (err) console.log('error', err);
});

const fileB = fs.readFileSync(process.argv[3], 'utf8', function (err, res) {
  if (err) console.log('error', err);
});

fs.writeFileSync(process.argv[4], fileA.concat(fileB), 'utf8', function (err, res) {
  if (err) console.log('error', err);
});

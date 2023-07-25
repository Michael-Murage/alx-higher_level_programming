#!/usr/bin/node
const fs = require('fs');

const arg = process.argv[2];

try {
  const fileRead = fs.readFileSync(arg, { encoding: 'utf-8' }, (err) => {
    console.log(err);
  });

  console.log(fileRead);
} catch (error) {
  console.log(error);
}

#!/usr/bin/node
const fs = require('fs');

const path = process.argv[2];
const content = process.argv[3];

try {
  const fileRead = fs.writeFileSync(path, content, { encoding: 'utf-8' });
} catch (error) {
  console.log(error);
}

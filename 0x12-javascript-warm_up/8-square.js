#!/usr/bin/node
const arg = process.argv[2];

if (!arg || !parseInt(arg)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < parseInt(arg); j++) {
    console.log('X'.repeat(arg));
  }
}

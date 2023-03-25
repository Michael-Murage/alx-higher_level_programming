#!/usr/bin/node
const args = process.argv;

try {
  if (args[2]) {
    console.log(args[2]);
  } else {
    console.log('No argument');
  }
} catch (error) {
  console.log('No argument');
}

#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const arr = args.slice(2).map((a) => parseInt(a));
  const secondLargest = arr.sort((a, b) => b - a)[1];
  console.log(secondLargest);
}

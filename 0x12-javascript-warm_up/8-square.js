#!/usr/bin/node
const n = Number(process.argv[2]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    const x = [];
    for (let j = 0; j < n; j++) {
      x.push('X');
    }
    console.log(x.join(''));
  }
}

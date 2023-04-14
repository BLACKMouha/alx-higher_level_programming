#!/usr/bin/node

const n = Math.floor(Number(process.argv[2]));

if (isNaN(n)) {
  console.log('Missing size');
} else {
  const s = 'X'.repeat(n);
  for (let i = 0; i < n; i++) {
    console.log(s);
  }
}

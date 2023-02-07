#!/usr/bin/node
const n = Number(process.argv[2]);
let r = 1;
if (isNaN(n) || n === 0 || n === 1) {
  console.log(r);
} else {
  for (let i = 2; i <= n; i++) {
    r *= i;
  }
  console.log(r);
}

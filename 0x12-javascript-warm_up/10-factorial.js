#!/usr/bin/node
function factorial (a) {
  const n = Number(a);
  let r = 1;

  if (isNaN(n) || n === 0 || n === 1) {
    console.log(r);
  }
  else {
    for (let i = 2; i <= n; i++) {
      r *= i;
    }
    console.log(r);
  }
}

factorial(process.argv[2]);

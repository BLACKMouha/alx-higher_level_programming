#!/usr/bin/node

if (process.argv.lenght < 4) {
  console.log('0');
} else {
  const arr = [];
  for (let i = 2; process.argv[i]; i++) {
    arr.push(Math.floor(Number(process.argv[i])));
  }
  arr.sort((a, b) => (b - a));
  console.log(arr[1]);
}

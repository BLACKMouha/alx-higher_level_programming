#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = [];
  process.argv.forEach((val, index) => {
    if (index >= 2) {
      arr.push(Number(val));
    }
  });
  arr.sort(function (a, b) {
    return a - b;
  });
  console.log(arr.reverse()[1]);
}

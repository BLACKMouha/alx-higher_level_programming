#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = [];
  process.argv.forEach((val, index) => {
    if (index >= 2) {
      arr.push(val);
    }
  });
  console.log(arr.reverse(arr.sort())[1]);
}

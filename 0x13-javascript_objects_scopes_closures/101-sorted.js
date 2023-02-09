#!/usr/bin/node
const dict = require('./101-data').dict;
const r = {};
for (const key in dict) {
  r[dict[key]] = [];
  for (const k in dict) {
    if (dict[k] === dict[key]) {
      r[dict[key]].push(k);
    }
  }
}
console.log(r);

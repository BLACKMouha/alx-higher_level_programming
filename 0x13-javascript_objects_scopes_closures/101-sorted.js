#!/usr/bin/node

const { dict } = require('./101-data');
const copyDict = Object.assign({}, dict);
const newDict = {};
for (const n in copyDict) {
  const tmp = copyDict[n];
  let list = [];
  for (const m in copyDict) {
    if (copyDict[m] === tmp) {
      list.push(m);
      delete copyDict[m];
    }
  }
  newDict[tmp] = list;
  list = [];
}
console.log(newDict);

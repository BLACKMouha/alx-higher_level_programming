#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((x, i = 0) => x * i);
console.log(newList);

#!/usr/bin/node
let y = 0;
const list = require('./100-data').list;
const lMap = list.map(x => x * y++);
console.log(list);
console.log(lMap);

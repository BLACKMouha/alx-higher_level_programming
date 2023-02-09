#!/usr/bin/node
const fs = require('fs');

fs.readFile('fileA', function (errA, dataA) {
  if (errA) throw errA;

  fs.readFile('fileB', function (errB, dataB) {
    if (errB) throw errB;

    dataA = dataA.toString();
    dataB = dataB.toString();

    fs.writeFile('fileC', dataA.concat(dataB), function (errC) {
      if (errC) throw errC;
    });
  });
});

#!/usr/bin/node

if (process.argv.length === 4) {
  const fs = require('fs');

  const path = process.argv[2];
  const content = process.argv[3].toString();

  fs.writeFile(path, content, (err) => {
    if (err) throw err;
  });
}

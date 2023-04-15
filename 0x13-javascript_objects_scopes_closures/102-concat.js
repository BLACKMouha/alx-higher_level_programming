#!/usr/bin/node
if (process.argv.length === 5) {
  const fs = require('fs');
  const contentA = fs.readFileSync(process.argv[2], 'utf-8');
  const contentB = fs.readFileSync(process.argv[3], 'utf-8');
  const contentC = contentA + contentB;
  fs.writeFile(process.argv[4], contentC, (err) => {
    if (err) throw err;
  });
}

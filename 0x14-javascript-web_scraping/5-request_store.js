#!/usr/bin/node
if (process.argv.length === 4) {
  const fs = require('fs');
  const request = require('request');

  const url = process.argv[2];
  const file = process.argv[3];

  request(url).pipe(fs.createWriteStream(file));
}

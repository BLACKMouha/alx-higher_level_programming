#!/usr/bin/node
/**
 * Writes a string to a file
 * the first argument is the file path
 * the second argument is the string to write
 * the content of the file must be written in utf-8
 * if an error occured during while writing, print the error object
 */

if (process.argv.length === 4) {
  const fs = require('fs');
  const f = process.argv[2];
  const c = process.argv[3];
  fs.writeFile(f, c, 'utf-8', function (e) {
    if (e) throw (e); else console.log(c);
  });
}

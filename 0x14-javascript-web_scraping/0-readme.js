#!/usr/bin/node
/**
 * Reads and Prints the content of a file
 * the first argument is the file path
 * if an error occured during the reading, prints the error object
 */
if (process.argv.length === 3) {
  const fs = require('fs');

  fs.readFile(process.argv[2], 'utf-8', function (e, c) {
    if (e) {
      console.error('Error occured while reading the file', e);
    } else {
      console.log(c);
    }
  });
}

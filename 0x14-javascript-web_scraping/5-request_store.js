#!/usr/bin/node
/**
 * Gets the contents of a webpage and stores it in a UTF-8 file.
 * The first argument is the URL to request
 * The second argument is the file path to store the body response
 * Uses the module 'request'
 */

if (process.argv.length === 4) {
  const request = require('request');
  const fs = require('fs');
  const url = process.argv[2];
  const f = process.argv[3];

  request.get(url, function (e, r, b) {
    if (e) {
      throw e;
    } else {
      fs.writeFile(f, b, 'utf-8', function (e) {
        if (e) throw (e);
      });
    }
  });
}

#!/usr/bin/node
/**
 * Displays the status code of a GET request
 * The first argument is the URL to request(GET)
 * The status code must be printed like this: 'code: <status code>
 * Uses the module 'request'
 */

if (process.argv.length === 3) {
  const request = require('request');
  const url = process.argv[2];
  request.get(url, function (e, r, b) {
    if (e) throw e; else console.log('code:', r.statusCode);
  });
}

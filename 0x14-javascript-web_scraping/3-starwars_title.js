#!/usr/bin/node
/**
 * Prints the titl of a Star Wars movie where the episode number matches
 * a given integer.
 * The first argument is the movie ID
 * Uses the Star Wars API and the module 'request'
 */

if (process.argv.length === 3) {
  const request = require('request');
  const id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
  request.get(url, function (e, r, b) {
    if (e) {
      throw e;
    } else {
      console.log(JSON.parse(b).title);
    }
  });
}

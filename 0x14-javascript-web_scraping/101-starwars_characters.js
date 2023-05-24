#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie, one by line
 * The first argument is an integer, the Movie ID
 * Used the Star Wars API and the module 'request'
 */

if (process.argv.length === 3) {
  const request = require('request');
  const id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

  request.get(url, function (e, r, b) {
    if (e) {
      throw (e);
    } else {
		const g = JSON.parse(b).characters;
		g.map(p => {
			request.get(p, function (x, s, m) {
				if (x) {
					throw (x);
				} else {
					console.log(JSON.parse(m).name);
				}
			});
		});
	}
  });
}

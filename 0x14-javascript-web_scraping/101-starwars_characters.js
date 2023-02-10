#!/usr/bin/node

if (process.argv.length === 3) {
  const request = require('request');

  const id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(id);

  request(url, function (error, response, body) {
    if (error !== null) console.log('error:', error);
    const characters = JSON.parse(body).characters;

    for (const character of characters) {
      request(character, function (err, res, bod) {
        if (err !== null) console.log('error:', err);
        const name = JSON.parse(bod).name;
        console.log(name);
      });
    }
  });
}

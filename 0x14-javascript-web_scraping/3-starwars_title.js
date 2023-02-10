#!/usr/bin/node

if (process.argv.length === 3) {
  const request = require('request');

  const id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(id);
  request(url, function (error, response, body) {
    if (error) console.log('error:', error);
    if (response.statusCode === 404) {
      console.log('statusCode:', response.statusCode);
    }
    console.log(JSON.parse(body).title);
  });
}

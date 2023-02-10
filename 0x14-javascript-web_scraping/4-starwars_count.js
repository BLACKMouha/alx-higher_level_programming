#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, function (error, response, body) {
  if (error) console.log('error:', error);
  if (response.statusCode === 404) {
    console.log('statusCode:', response.statusCode);
  }
  const results = JSON.parse(body).results;
  let c = 0;
  for (const result of results) {
    const characters = result.characters;
    for (const character of characters) {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') c += 1;
    }
  }
  console.log(c);
});

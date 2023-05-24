#!/usr/bin/node
/**
 * Computes the number of tasks completed by user id
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Uses the module 'requests'
 */

if (process.argv.length === 3) {
  const request = require('request');
  const url = process.argv[2];

  request.get(url, function (e, r, b) {
    if (e) {
      throw (e);
    } else {
      b = JSON.parse(b);
      const countDoneTasksByUserId = b.reduce((c, t) => {
        if (t.completed) {
          c[t.userId] = (c[t.userId] || 0) + 1;
        }
        return c;
      }, {});
      console.log(countDoneTasksByUserId);
    }
  });
}

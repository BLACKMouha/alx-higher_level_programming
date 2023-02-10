#!/usr/bin/node

if (process.argv.length === 3) {
  const request = require('request');

  const url = process.argv[2];

  request(url, function (error, response, body) {
    if (error !== null) console.log('error:', error);
    const data = JSON.parse(body);

    const completedTasksPerUser = {};
    for (const i of data) {
      let count = 0;
      for (const j of data) {
        if (j.userId === i.userId) {
          if (j.completed === true) count += 1;
        }
      }
      completedTasksPerUser[i.userId] = count;
    }
    console.log(completedTasksPerUser);
  });
}

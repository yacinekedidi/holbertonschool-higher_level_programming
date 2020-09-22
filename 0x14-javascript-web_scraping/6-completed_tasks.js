#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');
const d = {};

request(myArgs[0], function (err, resp, body) {
  const info = JSON.parse(body);
  err && console.log(err);
  for (let i = 0; i < info.length; i++) {
    if (info[i].completed) {
      if (d[info[i].userId]) { d[info[i].userId] += 1; } else { d[info[i].userId] = 1; }
    }
  }
  console.log(d);
});

#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');
let count = 0;

request(myArgs[0], function (err, resp, body) {
  const info = JSON.parse(body);
  err && console.log(err);
  for (let i = 0; i < info.results.length; i++) {
    for (let j = 0; j < info.results[i].characters.length; j++) {
      if (info.results[i].characters[j].includes('18')) { count++; }
    }
  }
  console.log(count);
});

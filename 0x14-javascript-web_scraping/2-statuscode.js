#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');

request(myArgs[0], function (err, resp, body) {
  err && console.log(err);
  resp && console.log('code: ' + resp.statusCode);
});

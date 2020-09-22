#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];

request(url, function (err, resp, body) {
  const info = JSON.parse(body);
  err && console.log(err);
  resp && console.log(info.title);
});

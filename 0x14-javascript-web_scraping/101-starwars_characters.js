#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);

const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];

request(url, function (err, resp, body) {
  err && console.log(err);
  const info = JSON.parse(body);
  for (let i = 0; i < info.characters.length; i++) {
    request(info.characters[i], function (err, resp, body) {
      const character = JSON.parse(body);
      !err && console.log(character.name);
    });
  }
});

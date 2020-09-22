#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');
const fs = require('fs');

request(myArgs[0]).pipe(fs.createWriteStream(myArgs[1]));

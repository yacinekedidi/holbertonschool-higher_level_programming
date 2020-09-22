#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');

fs.readFile(myArgs[0], 'utf-8', function (err, data) { console.log(err || data); });

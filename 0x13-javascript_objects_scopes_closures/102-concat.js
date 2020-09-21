#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');

const f1 = fs.readFileSync(myArgs[0]);
const f2 = fs.readFileSync(myArgs[1]);
fs.writeFileSync(myArgs[2], f1 + f2);

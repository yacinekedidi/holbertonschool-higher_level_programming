#!/usr/bin/node
var myArgs = process.argv.slice(2);
var l = myArgs.length;
var a;
if (l === 0) {
  a = 'No argument';
} else if (l === 1) {
  a = 'Argument found';
} else {
  a = 'Arguments found';
}
console.log(a);

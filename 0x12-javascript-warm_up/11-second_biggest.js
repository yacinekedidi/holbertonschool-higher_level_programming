#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length <= 1) {
  console.log(0);
} else {
  myArgs.sort().reverse();
  console.log(myArgs[1]);
}

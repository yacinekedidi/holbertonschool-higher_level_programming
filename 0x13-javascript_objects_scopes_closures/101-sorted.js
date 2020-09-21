#!/usr/bin/node
const d = require('./101-data').dict;
const l = Object.values(d);
const ll = l.filter(function (item, pos) {
  return l.indexOf(item) === pos;
});

const dd = {};
const keys = Object.keys(d);

for (const i in ll) {
  const x = [];
  for (const j in keys) {
    if (d[keys[j]] === ll[i]) {
      x.push(keys[j]);
      dd[ll[i]] = x;
    }
  }
}
console.log(dd);

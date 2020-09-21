#!/usr/bin/node
exports.esrever = function (list) {
  const l = [];
  let j = list.length - 1;
  for (let i = 0; i < list.length; i++, j--) {
    l[i] = list[j];
  }
  return l;
};

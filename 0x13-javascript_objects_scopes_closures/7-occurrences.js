#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter(c => c === searchElement).length;
};

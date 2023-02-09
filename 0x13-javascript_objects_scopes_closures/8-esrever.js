#!/usr/bin/node
exports.esrever = function (list) {
  r = [];
  for (let i = list.length - 1; list[i]; i--) {
    r.push(list[i]);
  }
  return (r);
}

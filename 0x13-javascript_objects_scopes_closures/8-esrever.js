#!/usr/bin/node
exports.esrever = function (list) {
  const r = [];
  for (let i = list.length - 1; list[i]; i--) {
    r.push(list[i]);
  }
  return (r);
};

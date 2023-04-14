#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  len--;
  for (let i = 0; i < len; i++) {
    const tmp = list[i];
    list[i] = list[len];
    list[len] = tmp;
    len--;
  }
  return (list);
};

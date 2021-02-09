#!/usr/bin/node
// reverse a list

exports.esrever = function (list) {
  const ret = [];
  for (let i = list.length - 1; i >= 0; i--) {
    ret.push(list[i]);
  }
  return ret;
};

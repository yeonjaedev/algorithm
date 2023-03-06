"use strict";

var solution = function solution() {
  var graph = [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]];
  var visited = graph.map(function (row) {
    return row.map(false);
  });
  console.log(visited);
};

solution();
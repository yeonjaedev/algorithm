// https://school.programmers.co.kr/learn/courses/30/lessons/12939
// 최댓값과 최솟값

function solution(s) {
  var answer = "";
  var numArr = s.split(" ").map((str) => Number(str));
  var min = numArr[0];
  var max = numArr[0];
  numArr.forEach((num) => {
    if (num < min) {
      min = num;
    }
    if (num > max) {
      max = num;
    }
  });
  return min + " " + max;
}

// https://school.programmers.co.kr/learn/courses/30/lessons/12941
// 최솟값 만들기
function solution(A, B) {
  var answer = 0;
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  for (var i = 0; i < A.length; i++) {
    answer += A[i] * B[i];
  }
  return answer;
}

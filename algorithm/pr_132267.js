function solution(a, b, n) {
  var answer = 0;
  while (n >= a) {
    receivedCoke = parseInt(n / a) * b;
    answer += receivedCoke;
    n = receivedCoke + (n % a);
  }
  return answer;
}

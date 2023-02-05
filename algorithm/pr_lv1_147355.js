// 크기가 작은 부분 문자열
// https://school.programmers.co.kr/learn/courses/30/lessons/147355
function solution(t, p) {
    var answer = 0;
    for(var i = 0; i <= t.length-p.length; i++){
        if(Number(t.slice(i,i+p.length)) <= Number(p)) { answer += 1}
    }
    return answer;
}
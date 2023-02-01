// 연속 부분 수열 합의 개수
// https://school.programmers.co.kr/learn/courses/30/lessons/131701
function solution(elements) {
    var answer = new Set()
    var nelements = [...elements,...elements]
    for(i=0;i<elements.length;i++){
        for(j=0;j<elements.length;j++){
            answer.add(nelements.slice(j, j + i).reduce((a,b)=>a+b,0))
        }      
    }
   return answer.size
}
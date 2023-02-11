// k진수에서 소수 개수 구하기
// https://school.programmers.co.kr/learn/courses/30/lessons/92335
function solution(n, k) {
    var answer = 0;
    var resultStr = '' // k진수로 바꾼 값
    const isPrime = (num) =>{
        if(num === 1 || num === 0) return false
        for ( let i = 2 ; i <= Math.sqrt(num) ; i ++) {
            if( num % i === 0) return false
        }
        return true
    }
    for(let i = 0 ; n>0 ; i++ ){
        resultStr = n%k+resultStr
        n=Math.floor(n/k)
    }
    // resultStr = n.toString(k) -> k진법 구하는 함수
    resultStr.split('0').forEach(str=>{
        if(isPrime(str*1)) answer += 1

    })
    return answer;
}
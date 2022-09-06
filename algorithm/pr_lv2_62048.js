// https://school.programmers.co.kr/learn/courses/30/lessons/62048
// 멀쩡한 사각형
// 그림 그려보기, 1씩 증가시키며 순차적으로 규칙찾기
// 최대공약수 구하는 공식

function solution(w, h) {
    return w*h-(w+h-gcd(w,h))
}
function gcd(w,h) {
    let minNum = Math.min(w,h)
    let gcdNum = 1
    for( i = 2; i<=minNum;i++){
        if (w%i===0 && h%i===0){
            gcdNum = i
        }
    }
    return gcdNum
}
// 롤케이크 자르기
// https://school.programmers.co.kr/learn/courses/30/lessons/132265

function solution(topping) {
    let answer = 0;
    let toppingCounter = new Map()
    let brother = new Map()
    topping.forEach((t)=>{ // topping 별 count 
        toppingCounter.set(t, (toppingCounter.get(t)||0) +1) 
    })
    topping.forEach((t,index)=>{
        toppingCounter.set(t, toppingCounter.get(t)-1) 
        // toppingCounter의 count를 하나씩 줄인다.
        if(!toppingCounter.get(t)){toppingCounter.delete(t)}
        // toppingCounter의 count가 0이되면 삭제한다.
        brother.set(t, (brother.get(t)||0) +1)
        // brother은 하나씩 증가시킨다.
        if(toppingCounter.size === brother.size) answer += 1
        // 둘의 size를 체크한다. 둘의 size가 같으면 종류가 같다는 의미이므로 answer을 증가시킨다.
        if(toppingCounter.size < brother.size) return answer
        // brother의 size가 커지면 공평하게 나뉘는게 불가능하므로 종료시킨다.
    })
    return answer
}
// 주차 요금 계산
// https://school.programmers.co.kr/learn/courses/30/lessons/92341
function solution(fees, records) {
    var answer = [];
    var carList = []
    records.forEach((record)=>{
        let car = record.slice(6,10)
        if(!carList.includes(car)){
            carList.push(car)
        }
    })
    carList = carList.sort()
    carList.map((car)=>{
        let timeList = records.filter((record)=>record.slice(6,10)===car).map(a=>a.slice(0,5))
        let totalCharge = 0
        let min = 0
        for(let i =0; i<timeList.length; i+=2){
            let hourVal = 0
            let minVal = 0
            if(timeList[i+1]){
                hourVal = Number(timeList[i+1].slice(0,2))-Number(timeList[i].slice(0,2))
                minVal = Number(timeList[i+1].slice(3,5))-Number(timeList[i].slice(3,5))
             }else { // i+1이 없으면 나간 기록이 없는 차량 23:59에서 빼기
                hourVal = 23-Number(timeList[i].slice(0,2))
                minVal = 59-Number(timeList[i].slice(3,5))
            }
            if(minVal < 0){ // 분이 음수라면 시간에서 1빼고 분에 60더하기
                minVal += 60
                hourVal -=1
            }
            min += hourVal*60 + minVal
            
        }
        
        totalCharge = (min-fees[0])/fees[2] > 0 ?  Math.ceil((min-fees[0])/fees[2]) * fees[3] + fees[1] : fees[1]
        answer.push(totalCharge)
    })
    
    return answer;
}
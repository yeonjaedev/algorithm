function solution(want, number, discount) {
    var answer = 0;
    var iter = 0
    var sum = 0
    var numberTemp = [...number]
    number.forEach(num => sum+= num)
    while(sum<=discount.length){
        for(i=iter;i<sum;i++){
            want.forEach((thing,idx)=>{
                if(thing == discount[i]){
                    number[idx] -= 1
                }
            })
        }
        answer += number.some((num)=>num>0) ? 0 : 1
        number = [...numberTemp]
        sum += 1
        iter += 1
    }
    
    return answer;
}
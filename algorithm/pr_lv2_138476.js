function solution(k, tangerine) {
    var answer = 0;
    var result = {};
    tangerine.forEach((x,idx) => { 
        result[x] = (result[x] || 0)+1; 
    });
    let countArr = Object.values(result).sort(function(a, b){return b - a})
    var i = 0
    while(k>0){
        k -= countArr[i]
        answer += 1
        i++;
    }
    return answer;
   
}

//시간초과
function solution(k, tangerine) {
    var answer = 0;
    var count = [];
    tangerine.forEach((x) => { 
      result[x] = (result[x] || 0)+1; 
    });
    var uniqueArr = [...new Set(tangerine)]
    uniqueArr.forEach(item=>{
        var cnt = 0;
        tangerine.forEach(a=>{
            if (a === item){
                cnt += 1  
            }
        })
        count.push({item,cnt})
    })
   
    count.sort(function(a, b){
      return b.cnt - a.cnt
    })
    for (i = 0; i < count.length; i++) {
        k-=count[i].cnt
        answer+=1
        if(k<=0){
            break;
        }
    }
    return answer;
   
}

function solution(k, tangerine) {
    var answer = 0;
    var count = [];
    var result = {};
    tangerine.forEach((x,idx) => { 
        result[x] = (result[x] || 0)+1; 
    });
    let countArr = Object.keys(result).map((item) =>{return {'item':item,'cnt':result[item]}});
    
    countArr.sort(function(a, b){
      return b.cnt - a.cnt
    })
    for (i = 0; i < countArr.length; i++) {
        k-=countArr[i].cnt
        answer+=1
        if(k<=0){
            break;
        }
    }
    return answer;
   
}


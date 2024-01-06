const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const [n,...arr] = input;
arr.forEach((val,index)=>{
    res = 0
    val.split(' ').map(num => res += parseInt(num))
    console.log(`Case #${index+1}: ${res}`)
})
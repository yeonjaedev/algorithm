const input = require('fs').readFileSync('dev/stdin').toString().trim().split('\n')
const [...arr] = input;
arr.forEach(val=>{
    res = 0
    val.split(' ').map(num => res += parseInt(num))
    if(res == 0) return
    console.log(res)
})
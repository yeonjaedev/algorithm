const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
let res = 0
const arr = input.map(a => res += parseInt(a))
console.log(res)
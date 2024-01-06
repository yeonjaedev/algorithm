const input = require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim()
const num = parseInt(input)
let str = ''
for(let i = 1;i<=num;i++){
    str += `${i}\n`
}
console.log(str)
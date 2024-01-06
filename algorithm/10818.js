const input = require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim().slice(1).slice(1).split(' ').map(s => parseInt(s))

let min = input[0]
let max = input[0]
for(let i = 0; i<input.length; i++){
  if(min > input[i]) min = input[i]
  if(max < input[i]) max = input[i]
}
console.log(`${min} ${max}`)



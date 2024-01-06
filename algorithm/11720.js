const input = require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .slice(1);

let sum = 0

input[0].split('').map(s => sum += parseInt(s))
console.log(sum)

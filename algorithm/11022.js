const input = require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .slice(1)
  .map((string) => string.split(' ').map(Number));

input.forEach(([a,b],i)=>console.log(`Case #${i+1}: ${a} + ${b} = ${a+b}`))


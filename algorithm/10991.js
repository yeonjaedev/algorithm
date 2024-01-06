const input = parseInt(require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim())

for(let i = 0; i < input; i++){
  console.log(' '.repeat(input-i-1)+'* '.repeat(i+1))
}
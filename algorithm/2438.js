const input = parseInt(require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim())

let str = ''
for(let i = 1;i<=input;i++){
  str += '*'
  console.log(str)
}
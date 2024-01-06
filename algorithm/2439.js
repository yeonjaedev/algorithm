const input = parseInt(require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim())


for(let i = 1;i<=input;i++){
  console.log(" ".repeat(input-i)+"*".repeat(i))
}
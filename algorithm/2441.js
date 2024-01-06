const input = parseInt(require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim())

for(let i =input;i>0;i--){
  console.log(" ".repeat(input-i)+"*".repeat(i))

}
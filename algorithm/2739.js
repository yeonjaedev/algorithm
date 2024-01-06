const input = parseInt(require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim())
for(let i = 1;i<=9;i++){
    console.log(`${input} * ${i} = ${input*i}`)
}
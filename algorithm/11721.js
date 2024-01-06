const input = require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim()

for(let i =0;i<input.length;i+=10){
    console.log(input.slice(i,i+10))
}

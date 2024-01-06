const input = parseInt(require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim())


const num = 2*input-1
for(let i = 1; i<=num; i++){
  if(i <= input){
    console.log(' '.repeat(input-i)+'*'.repeat(i))
  }else {
    console.log(' '.repeat(i-input)+'*'.repeat(num-i+1))
  }
}
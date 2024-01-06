const input = parseInt(require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim())


const num = 2*input-1
for(let i = 0; i<num; i++){
  if(i < input){
    console.log(' '.repeat(i)+'*'.repeat(num-2*i))
  }else {
    console.log(' '.repeat(-1*i+num-1)+'*'.repeat(2*i-num+2))

  }
}
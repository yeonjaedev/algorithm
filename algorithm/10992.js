const input = parseInt(require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim())

for(let i = 0;i<input-1;i++){
  if(i==0){
    console.log(' '.repeat(input-i-1)+'*')
  } else {
    console.log(' '.repeat(input-i-1)+'*'+' '.repeat(2*i-1)+'*')
  }
  
}
console.log('*'.repeat(2*input-1))
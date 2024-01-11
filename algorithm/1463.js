const input = parseInt(require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim())

let arr = [0,0,1,1]

for(let i = 4; i<=input; i++){
  arr[i] = Math.min(
    i%3==0?arr[Math.floor(i/3)]:1000000,
    i%2==0?arr[Math.floor(i/2)]:1000000,
    arr[i-1]
  ) + 1
}
console.log(arr[input])
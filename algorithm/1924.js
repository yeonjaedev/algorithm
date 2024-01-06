const input = require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .trim()
  .split(' ')
  .map(s=>parseInt(s))

const days = [31,28,31,30,31,30,31,31,30,31,30,31]
const day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

let dates = 0
const month = input[0]-1
const date = input[1]
for(let i =0; i<month;i++){
  dates += days[i]
  
}
dates += date
console.log(day[dates % 7])
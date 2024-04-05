let [num,...input] = require('fs')
    .readFileSync('/dev/stdin', 'utf-8')
    .trim()
    .split('\n')
    .map((s) => Number(s));

let sorted = input.sort((a,b)=>a-b)
console.log(sorted.join("\n"))
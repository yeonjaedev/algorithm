let [num,...input] = require('fs')
    .readFileSync('/dev/stdin', 'utf-8')
    .trim()
    .split('\n')
    .map((s) => s.split(' '));

let res = input.sort((a,b)=>Number(a[0])-Number(b[0]))
console.log(res.join('\n').replaceAll(',',' '))
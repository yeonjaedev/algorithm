let [num,...input] = require('fs')
    .readFileSync('/dev/stdin', 'utf-8')
    .trim()
    .split('\n')
    .map((s) => s.split(' ').map(x=>Number(x)));

let sorted = input.sort((a,b)=>{
    if(a[1] === b[1]){
        return a[0] - b[0]
    } else {
        return a[1] - b[1]
    }
})
console.log(sorted.join('\n').replaceAll(',',' '))
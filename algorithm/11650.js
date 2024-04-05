let [num,...input] = require('fs')
    .readFileSync('/dev/stdin', 'utf-8')
    .trim()
    .split('\n')
    .map((s) => s.split(' ').map(x=>Number(x)));

let sorted = input.sort((a,b)=>{
    if(a[0] === b[0]){
        return a[1] - b[1]
    } else {
        return a[0] - b[0]
    }
})
console.log(sorted.join('\n').replaceAll(',',' '))
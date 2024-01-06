const input = require('fs')
  .readFileSync('/dev/stdin', 'utf-8')
  .split('\n')
  .map((string) => console.log(string));
for(let i = 0;i<n;i++){
  //   for(let j=0;j<m;j++){
  //     console.log(i,j)
  //     console.log((i-1>=0 && j-1>=0) ? array[i-1][j-1] : 0,
  //     j-1 >= 0 ? array[i][j-1] : 0,
  //     (i+1 < n && j-1 >= 0) ? array[i+1][j-1] : 0)
  //     console.log('max',Math.max(
  //       (i-1>=0 && j-1>=0) ? array[i-1][j-1] : 0,
  //     j-1 >= 0 ? array[i][j-1] : 0,
  //     (i+1 < n && j-1 >= 0) ? array[i+1][j-1] : 0
  //     ))

  //     dp[i][j] = array[i][j] + Math.max(
  //       (i-1>=0 && j-1>=0) ? array[i-1][j-1] : 0,
  //       j-1 >= 0 ? array[i][j-1] : 0,
  //       (i+1 < n && j-1 >= 0) ? array[i+1][j-1] : 0
  //       )
  //   }
  // }
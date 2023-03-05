const dfs = (graph,num,isChecked) => {
    isChecked[num] = true
    console.log(num,' ')
    let arr = graph[num]
    arr.forEach(a=>{
        if(!isChecked[a]){
            dfs(graph,a,isChecked)
        }
    })
}

const solve = () => {
    const graph = [
        [],
        [2,3,8], // 1와 연결된 노드
        [1,7], // 2와 연결된 노드
        [1,4,5], // 3과 연결된 노드
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]
    let isChecked = Array(graph.length).fill(false);
    
    dfs(graph,1,isChecked)
}
solve()
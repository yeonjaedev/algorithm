const bfs = (graph,num) => {
    let queue = [num]
    
    let visited = Array(graph.length).fill(false);
    visited[num] = true
    while(queue){
        let out = queue.shift()
        
        if(!out){
            return
        }
        console.log(out,' ')
       
        graph[out].forEach(g=>{
            if(!visited[g]) {
                queue.push(g) // 넣은 것은 어차피 방문할꺼니까 true로
                visited[g] = true
            }
        })
    }
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
    
    bfs(graph,1)
}
solve()
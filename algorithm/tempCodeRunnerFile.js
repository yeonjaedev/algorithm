graph[out].forEach(g=>{
            if(!visited[g]) {
                queue.push(g)
                visited[g] = true
            }
        })
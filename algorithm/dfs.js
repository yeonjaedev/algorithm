const graph = {
    A: ["B", "C"],
    B: ["A", "D"],
    C: ["A", "G", "H", "I"],
    D: ["B", "E", "F"],
    E: ["D"],
    F: ["D"],
    G: ["C"],
    H: ["C"],
    I: ["C", "J"],
    J: ["I"]
};

const DFS = (graph, startNode) => {
    const visited = []
    let willVisit = []
    willVisit.push(startNode)
    while(willVisit.length !== 0) {
        let node = willVisit.shift()
        if(!visited.includes(node)){
            visited.push(node)
            willVisit = [...graph[node],...willVisit]
        }
    }
    return visited
}
console.log(DFS(graph,'A'))
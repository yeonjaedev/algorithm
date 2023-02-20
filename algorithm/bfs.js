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
    
const BFS = (graph,startNode) => {
    const visitedList = [] // 탐색을 마친 노드들
    let willVisitList = [] // 탐색해야할 노드들

    willVisitList.push(startNode) 

    while(willVisitList.length !== 0) { // 탐색해야할 노드가 남아있다면
        const node = willVisitList.shift() // 제일 첫번째 노드를 빼내기
        if(!visitedList.includes(node)) { // 방문한적이 없다면
            visitedList.push(node) // 방문
            willVisitList = [...willVisitList, ...graph[node]] 
        }
    }
    return visitedList
}

console.log(BFS(graph,'A'))


// 백준 1926 그림
// https://www.acmicpc.net/problem/1926
// BFS 기초문제

const n = 6
const m = 5
const graph = [
    [ 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1]
]
let visited = graph.map(row => row.map(r => {return false}))
const solution = () => {
    let count = 0
    let maxCount = 0
    for(let i = 0; i < n; i++){   
        for(let j = 0; j < m ; j++){
            if(graph[i][j] === 1 && !visited[i][j]){
                visited[i][j] = true
                count += 1 // 전체 그림 개수 + 1
                maxCount = Math.max(bfs(i,j),maxCount) // 그림 크기 구해주고, 최대값 갱신
            }
        }
    }
    console.log(count)
    console.log(maxCount)
}
const bfs = (i,j) => {
    let queue = []
    let cnt = 1
    let dx = [0,1,0,-1] // 우,하,좌,상
    let dy = [1,0,-1,0] // 우,하,좌,상
    queue.push([i,j])
    while(queue.length){
        const [ex,ey] = queue.shift()
        for(let k = 0 ; k < 4 ; k++){
            const nx = ex + dx[k]
            const ny = ey + dy[k]
            if(0 <= nx && nx < n && ny >=0 && ny < m){ // x좌표는 n을 넘으면 안되고, y좌표는 m을 넘으면 안된다.
                if(graph[nx][ny] === 1 && !visited[nx][ny]){
                    visited[nx][ny] = true
                    cnt += 1
                    queue.push([nx,ny])
                }
            }
        }
    }
    return cnt
    
}
solution()
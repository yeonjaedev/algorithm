// https://school.programmers.co.kr/learn/courses/30/lessons/87946
// 피로도

// dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.
// 조건 크기가 작으면 완전탐색 고려하기
function solution(k, dungeons) {
    var answer = 0;
    const visited = Array(dungeons.length).fill(false);
    const dfs = (currentK, cnt) => {
        for(let i = 0; i < dungeons.length; i++) {
            // 해당 던전을 아직 방문하지 않았고
            // 던전의 최소 피로도가 현재 피로도보다 작거나 같으면
            if(!visited[i] && currentK >= dungeons[i][0]) {
            	// 해당 던전 방문표시
                visited[i] = true;
                // 재귀
                dfs(currentK - dungeons[i][1], cnt + 1);
                // DFS 종료 후 방문을 끝내준다.
                visited[i] = false;
            }
        }
        // 최대 던전 수 갱신
        answer = Math.max(answer, cnt);
        return;
    }

    dfs(k, 0);
    return answer;
}
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for i in range(n)]

# 시작점 탐색
deq = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            deq.append((i,j))

# 탐색하지 않은 좌표를 큐에 넣어준다.
# 좌표가 0일 때만 BFS를 실행하므로 
# 따로 방문 배열을 만들어주지 않아도 된다.
def bfs(point):
    for i in [-1,0],[1,0],[0,-1],[0,1]:
        x,y = point[0]+i[0], point[1]+i[1]
        if n > x >= 0 and m > y >= 0 and tomato[x][y] == 0:
            tomato[x][y] += tomato[point[0]][point[1]]+1
            deq.append((x,y))

# 시작점이 없을 경우 종료
if len(deq) == 0:
    print(-1)
    sys.exit(0)

# BFS 실행
while(deq):
    bfs(deq.popleft())

# BFS가 끝났는데도 익지 않은 토마토가 있다면 -1 출력
# 다 익었다면 tomato 배열 중 가장 큰 것 출력
r = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit(0)
        if j > r:
            r = j
print(r-1)
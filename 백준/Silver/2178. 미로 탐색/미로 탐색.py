from collections import deque

N, M = map(int, input().split())

graph = []

# 🔹 입력값이 "1011" 같은 형식이면 그대로 사용하고, "1 0 1 1" 같은 형식이면 split() 사용
for _ in range(N):
    graph.append(list(map(int, input().strip())))  # 🔹 띄어쓰기 없이 입력받도록 수정

def BFS(x, y): 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]  # 🔹 들여쓰기 수정

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1   

    return graph[N - 1][M - 1]  # 🔹 들여쓰기 수정

print(BFS(0, 0))

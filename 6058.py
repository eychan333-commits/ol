n = int(input())
r = [input() for _ in range(n)]
v = [[0]*n for _ in range(n)]
dx = [1, -1, 0, 0]
ans = 0
dy = [0, 0, 1, -1]
def dfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < n and 0 <= ny < n and r[ny][nx] == '1' and v[ny][nx] == 0:
            v[ny][nx] = 1
            dfs(ny, nx)


for i in range(n):
    for j in range(n):
        if r[i][j] == '1' and v[i][j] == 0:
            dfs(i, j)
            ans+=1
           
print(ans)
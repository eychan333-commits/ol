from collections import deque
n = int(input())
r = [list(map(int, list(input().strip()))) for _ in range(n)]
v = [[0]*n for _ in range(n)]
cnt=0
q = deque()
q.append((0,0))
l=[]
ans=0  #단지수
def bfs(i,j):
    q.append((i,j))
    global cnt
    cnt=0
    while q:
        y,x = q.popleft()
        for xy,xx in zip((1,-1,0,0),(0,0,1,-1)):
            ny = y+xy
            nx = x+xx
            if 0 <= ny < n and 0<=nx<n and v[ny][nx] == 0 and r[ny][nx] == 1:
                cnt+=1
                v[ny][nx] = 1
                q.append((ny,nx))

for i in range(n): 
    for j in range(n):
        if r[i][j] == 1 and v[i][j] == 0:
    
            bfs(i,j)
            l.append(cnt)
            ans+=1

print(ans)
l.sort()
for j in range(len(l)):
    if l[j] == 0:
        print(1)
    else:
        print(l[j])
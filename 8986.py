from collections import deque
q=deque()
a,b=map(int,input().split())
l=[]

visited=[[0]*b for i in range(a)]
for i in range(a):
    d=input()
    l.append(d)
for i in range(a):
    if l[i][0]== '.' and visited[i][0]==0:
        visited[i][0]=1
        q.append((i,0))
ans=0       

z = list(zip([-1,1,0,0],[0,0,-1,1]))
while q:
    d,vv = q.popleft()
    for x, y in z:
        nx = vv+x
        ny = d+y
        if 0<=ny < a and 0<=nx < b and visited[ny][nx]==0 and l[ny][nx]=='.':
            visited[ny][nx]=visited[d][vv]+1
            q.append((ny,nx))

mm = a*b
for i in range(a):
    if visited[i][b-1]!=0 and visited[i][b-1]<mm:
        mm = visited[i][b-1]
    for j in range(b):
        if l[i][j]=='.':
            ans+=1

print(ans-mm)
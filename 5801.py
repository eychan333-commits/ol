from collections import deque
ans = 0
c = 0
cc = 0
dd = 0 
n = int(input())
q = deque()
a = list(map(int, input().split()))
for j in range(n):
    q.append(a[j])

for i in range(n):
    dd = q[0]
    while 0 < dd:
        
        cc = q.popleft()
        
        if cc == dd:
            dd-=1
            if dd == 0:
                ans+=1
                break
            else:
                q.append(dd)
        
        else:
            q.append(cc)
        q.rotate(-1)
        ans += 1
    print(ans)
  
  



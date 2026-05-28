from collections import deque
ans = 0
pizza = {}
p, n = map(int, input().split())
q = deque()
for i in range(n):
    o  = list(map(int, input().split()))
    if o[0] == 0:
        if o[1] not in pizza:
            pizza[o[1]] = deque()
        pizza[o[1]].append(o[2])
    else:
        if o[1] in pizza and pizza[o[1]]:
            ans += pizza[o[1]].popleft()

            pass

print(ans)


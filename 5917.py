a,b = map(int, input().split())
d = []
ee = []
if b == 0:
    for i in range(a):
        c = int(input())
        d.append(int(input(), sep = "\n"))
        
        solve(d)
elif b == 1:
    for i in range(a):
        c = int(input())
        d= input()
        solve1(d)  
def solve(d):
    for i in range(c):
        ee.append(d.pop())

        
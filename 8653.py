import sys
input = sys.stdin.readline
n, q = map(int, input().split())
l = list(map(int, input().split()))
l1 = l.index(max(l))
ei = max(l)
a = l[:l1]
b = l[l1 + 1:]
s = 0
e = 0
mid = 0

def ismid(x):
    if x == ei:
        print("T")
    else:
        return 0
def solve(x):
    s = 0
    e = l1-1
    while True:
        mid = (s+e)//2
        if a[mid] == x:
            print("L")
            break
        elif a[mid] < x:
            s = mid+1
        elif a[mid] > x:
            e = mid-1
        if s > e:
            return 0
def solve1(x):
    s = 0
    e = len(b)-1
    while True:
        mid = (s+e)//2
        if b[mid] == x:
            print("R")
            break
        elif b[mid] > x:
            s = mid+1
        else:
            e = mid-1
        if s > e:
            return 0
for i in range(q):
    x = int(input())
    if ismid(x) == 0 and solve(x) == 0 and solve1(x) == 0:
        print("N")

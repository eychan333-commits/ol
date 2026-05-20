q = int(input())
s = []
d = ''
for i in range(q):
    d = input()
    if d == 'READ':
        print(s.pop())
    else:
        s.append(d)
    
    d = ''

    
    
a,b = map(int, input().split())
d = ""


def solve1(c):

    ee = []
    ccc = ''
    eii = 0
    eie = ''
    cc = ''
    io = 0
    t = 0
    ccc = ''
    for _ in range(c):
        eii+=1
    
        ee.append(dd.pop())
       
       
        if eii == 1:
            eie = ee.pop()
            if eie == 'O':
                t += 1
            ee.append(eie)
        else:
            cc = ee.pop()
            io = t%2
            
            if io == 0 and cc == 'M':
                ee.append('M')
              
            elif io == 0 and cc == 'O':
                t+=1
                ee.append('O')
               
            else:
                if cc == 'O':
                    
                    ee.append('M')
                
                if cc == 'M':
                    t+=1
                    ee.append('O')
    ee.reverse()
    for x in ee:
        ccc+=x
    print("YES")   
    print(ccc)

if b == 0:
    for i in range(a):
        c = int(input())
        d = input()
        
        print("YES")
elif b == 1:
    for i in range(a):
        c = int(input())
        d = input()
        
        dd = list(d)
  
        solve1(c)
        dd = '' 


        
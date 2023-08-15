a = int(input())
m = []
for c in range(0 , a):
    b = int(input())
    m.append(b)
def sumlist(m):
    d = 0 
    for c in m : 
        d = d + c 
    return(d) 
print(sumlist(m))
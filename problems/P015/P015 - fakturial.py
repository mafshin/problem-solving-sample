a = int(input())
m = []
for d in range(2 , a):
    ispreme = True
    for e in range(2 , d):
        if d % e == 0:
            ispreme = False
    if ispreme:
        m.append(d)
def beat(m):
    b = 1
    for c in m:
        b = b * c
    return(b)
print(beat(m))
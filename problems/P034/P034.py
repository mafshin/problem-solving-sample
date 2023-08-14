a = int(input("int : "))
m = []
x1 = -1
A = 0
while A != len(str(a)):
    x2 = 1
    m.append(str(a)[x1])
    x1 += 1
    A += 1
    while True:
        if x2 >= len(str(a)):
            break
        x2 += 1
        if x1 != x2:
            if str(a)[x1:x2] != '':
                m.append(str(a)[x1:x2])
for b in m:
    if int(b) != 1:
        is_preme = True
        for d in range(2 , int(b)):
            if int(b) % d ==0:
                is_preme = False
        if is_preme:
                print(b)
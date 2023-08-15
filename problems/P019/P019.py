INPUT = int(input('int : '))
H = INPUT * 2
a = [1]
b = [1 , 1]
if len(a) <= INPUT:
    print('.' * H , a , '.' * H)
    H -= 1
if len(b) <= INPUT:
    print('.' * H , b , '.' * H)
while len(a) <= INPUT and len(b) <= INPUT:
    H -= 1
    a = [1]
    if len(b) <= INPUT:
        x = 0
        y = 1
        while y < len(b):
            a.append(b[x] + b[y])
            x += 1 
            y += 1
        a.append(1)
        if len(a) <= INPUT :
            print('.' * H , a , '.' * H)
            H -= 2
    if len(a) <= INPUT:
        b = [1]
        x = 0
        y = 1
        while y < len(a):
            b.append(a[x] + a[y])
            x += 1
            y += 1
        b.append(1)
        if len(b) <= INPUT:
            print('.' * H , b , '.' * H)
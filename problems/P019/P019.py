INPUT = int(input())
if INPUT <= 5:
    A = INPUT
    B = INPUT - 1
if INPUT >= 6:
    A = INPUT + 6
    B = INPUT + 4
a = [1]
b = [1 , 1]
if len(a) <= INPUT:
    print(' ' * A , a)
if len(b) <= INPUT:
    print(' ' * B , b)
if INPUT <= 5:
    H = INPUT - 1
if INPUT >= 6:
    H = INPUT + 5
while len(a) <= INPUT and len(b) <= INPUT:
    if INPUT <= 5:
        H = H - 1
    if INPUT >= 6:
        H = H - 2
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
            print(' ' * H , a)
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
            if INPUT <= 5:
                H = H - 1
            if INPUT >= 6:
                H = H - 2
            print(' ' * H , b)
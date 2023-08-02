a = int(input("input : "))
if a < 2:
    print(f"{a} < 2")
else:
    m = []
    for b in range(2 , a):
        is_preme = True
        for d in range(2 , b):
            if b % d ==0:
                is_preme = False
        if is_preme:
            m.append(b)
            for X in range(len(m)):
                for Y in range(1 , len(m)):
                    if m[X] + m[Y] == a:
                        if a % 2 ==0:
                            print(m[X] , m[Y])
                        if a % 2 !=0:
                            print(f"{a} is odd")
a = int(input())
for d in range(2 , a):
    ispreme = True
    for c in range(2 , d):
        if d % c == 0:
            ispreme = False
    if ispreme:
        print(d)
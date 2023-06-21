a = int(input())
m = []
for b in range(2 , a):
    ispreme = True
    for c in range(2 , b):
        if b % c == 0:
            ispreme = False
    if ispreme:
        m.append(b)
print(len(m))
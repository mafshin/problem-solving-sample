a = int(input('int : '))
n = []
for A in range(1 , a + 1):
    b = input(f'list {A} : ')
    n.append(b.split())
m = []
for w in range(len(n)):
    for x in n[w]:
        I = 0
        for W in range(1 , len(n)):
            for X in n[W]:
                if x == X:
                    I += 1
                    if I == a - 1:
                        if x not in list(map(lambda f: f[0] , m)):
                            m.append((x , I))
m.sort(key=lambda p: -1 * p[1])
ouput = []
for OUPUT in m:
    ouput.append(OUPUT[0])
print(" ".join(ouput))
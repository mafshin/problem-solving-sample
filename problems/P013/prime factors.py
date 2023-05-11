a = int(input())
def prime_list(a):
    m = []
    for d in range(2 , a):
        ispreme = True
        for c in range(2 , d):
            if d % c ==0:
              ispreme = False
        if ispreme:
            m.append(d)
    return m
b = prime_list(a)
n = []
for shirpharhad in b:
    while a % shirpharhad ==0:
        a = a / shirpharhad
        n.append(shirpharhad)
print(n)
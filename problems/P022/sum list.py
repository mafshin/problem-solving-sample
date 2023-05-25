a = int(input())
m = []
n = []
output = []
for A in range(1 , a + 1):
    b = int(input())
    m.append(b)
print('ـــــــــــ')
for B in range(1 , a + 1):
    d = int(input())
    n.append(d)
for x in range(1 , a + 1):
    D = m[x - 1] + n[x - 1]
    output.append(D)
print(output)
a = int(input())
m = []
A = 1
x = 0
while x < a:
    A = A + 1
    ispreme = True
    for B in range(2 , A):
        if A % B ==0:
            ispreme = False
    if ispreme:
        m.append(A)
        x = x + 1
print(m[x - 1])
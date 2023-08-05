a = int(input("int : "))
m = []
for A in range(0 , a):
    b = int(input(f"input {A + 1} : "))
    m.append(b)
H = 0
for total in m:
    H = H + total
I = 1
for beat in m:
    I = I * beat

Maxis = []
for MAX in range(1 , H):
    for max in range(1 , a):
        Max = m[max - 1]
        if Max == MAX:
            Maxis.append(Max)
Minis = []
for MIN in range(H , 0 , -1):
    for min in range(a , 0 , -1):
        Min = m[min - 1]
        if Min == MIN:
            Minis.append(Min)
Avgis = []
h = 1
for AVG in m:
    h = h +AVG
    Avgis.append(h)
h = int(h / len(Avgis))

lastthreenumbersareis = []
for lastthreenumbersare in range(len(m) - 3 , len(m)):
    lastthreenumbersareis.append(m[lastthreenumbersare])
    
print(f"Max is {int(Maxis[len(Maxis) - 1])}")
print(f"Min is {int(Minis[len(Minis) - 1])}")
print(f"Avg is {h}")
print(f"Last 3 numbers are is {lastthreenumbersareis}")
print(f"Sum of all is {H}")
print(f"Product of all is {I}")

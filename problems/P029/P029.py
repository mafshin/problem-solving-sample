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

Max_is = []
for MAX in range(1 , H):
    for max in range(1 , a):
        Max = m[max - 1]
        if Max == MAX:
            Max_is.append(Max)

Min_is = []
for MIN in range(H , 0 , -1):
    for min in range(a , 0 , -1):
        Min = m[min - 1]
        if Min == MIN:
            Min_is.append(Min)

Avg_is = []
h = 1
for AVG in m:
    h = h +AVG
    Avg_is.append(h)
h = int(h / len(Avg_is))

Last_three_numbers_are_is = []
for last_three_numbers_are in range(len(m) - 3 , len(m)):
    Last_three_numbers_are_is.append(m[last_three_numbers_are])
    
print(f"Max is {int(Max_is[len(Max_is) - 1])}")
print(f"Min is {int(Min_is[len(Min_is) - 1])}")
print(f"Avg is {h}")
print(f"Last 3 numbers are is {Last_three_numbers_are_is}")
print(f"Sum of all is {H}")
print(f"Product of all is {I}")
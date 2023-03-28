input = int(input())
print(1)
print(1)
a = 1
b = 1
for c in range(0 , input):
    a = a + b
    b = a + b
    if a < input:
        if b < input:
            print(a)
            print(b)